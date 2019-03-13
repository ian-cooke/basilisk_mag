/*
 ISC License
 
 Copyright (c) 2016-2017, Autonomous Vehicle Systems Lab, University of Colorado at Boulder
 
 Permission to use, copy, modify, and/or distribute this software for any
 purpose with or without fee is hereby granted, provided that the above
 copyright notice and this permission notice appear in all copies.
 
 THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 
 */
/*
 B_DOT Module
 
 */

#include "attControl/B_DOT/B_DOT.h"
#include "simulation/utilities/linearAlgebra.h"
#include "simulation/utilities/rigidBodyKinematics.h"
#include "simFswInterfaceMessages/macroDefinitions.h"
#include "fswUtilities/fswDefinitions.h"
#include "simulation/utilities/astroConstants.h"
#include "simulation/utilities/bsk_Print.h"
#include "simulation/utilities/mtx.h"
#include "simulation/utilities/linearAlgebra.h"
#include "fswMessages/rwAvailabilityFswMsg.h"


#include <string.h>
#include <math.h>

#include<stdlib.h>

/*! This method initializes the ConfigData for this module.
 It checks to ensure that the inputs are sane and then creates the
 output message
 @return void
 @param ConfigData The configuration data associated with this module
 */
void SelfInit_B_DOT(B_DOTConfig *ConfigData, uint64_t moduleID)
{
    
    /*! Begin method steps */
    /*! - Create output message for module */
    ConfigData->outputMsgID = CreateNewMessage(ConfigData->outputDataName,
                                               sizeof(CmdTorqueBodyIntMsg), "CmdTorqueBodyIntMsg", moduleID);

    
}

/*! This method performs the second stage of initialization for this module.
 It's primary function is to link the input messages that were created elsewhere.
 @return void
 @param ConfigData The configuration data associated with this module
 */
void CrossInit_B_DOT(B_DOTConfig *ConfigData, uint64_t moduleID)
{
    /*! - Get the control data message IDs*/
    ConfigData->vehConfigInMsgID = subscribeToMessage(ConfigData->vehConfigInMsgName,
                                                      sizeof(VehicleConfigFswMsg), moduleID);
    ConfigData->inputMagMeterID = subscribeToMessage(ConfigData->inputMagMeterName,
                                                     sizeof(MagMeterIntMsg), moduleID);


    ConfigData->rwParamsInMsgID = -1;
    ConfigData->inputRWSpeedsID = -1;
    ConfigData->rwAvailInMsgID = -1;

    if(strlen(ConfigData->rwParamsInMsgName) > 0) {
        ConfigData->rwParamsInMsgID = subscribeToMessage(ConfigData->rwParamsInMsgName,
                                                       sizeof(RWArrayConfigFswMsg), moduleID);
        if (strlen(ConfigData->inputRWSpeedsName) > 0) {
        ConfigData->inputRWSpeedsID = subscribeToMessage(ConfigData->inputRWSpeedsName,
                                                         sizeof(RWSpeedIntMsg), moduleID);
        } else {
            BSK_PRINT(MSG_ERROR, "Error: the inputRWSpeedsName wasn't set while rwParamsInMsgName was set.\n");
        }
        if(strlen(ConfigData->rwAvailInMsgName) > 0) {
            ConfigData->rwAvailInMsgID = subscribeToMessage(ConfigData->rwAvailInMsgName,
                                                             sizeof(RWAvailabilityFswMsg), moduleID);
        }
    }

}

/*! This method performs a complete reset of the module.  Local module variables that retain
 time varying states between function calls are reset to their default values.
 @return void
 @param ConfigData The configuration data associated with the MRP steering control
 */
void Reset_B_DOT(B_DOTConfig *ConfigData, uint64_t callTime, uint64_t moduleID)
{
    /*! - Read the input messages */
    uint64_t clockTime;
    uint32_t readSize;
    
    VehicleConfigFswMsg sc;
    ReadMessage(ConfigData->vehConfigInMsgID, &clockTime, &readSize,
                sizeof(VehicleConfigFswMsg), (void*) &(sc), moduleID);
    
    ConfigData->rwConfigParams.numRW = 0;
    if (ConfigData->rwParamsInMsgID >= 0) {
        /*! - Read static RW config data message and store it in module variables*/
        ReadMessage(ConfigData->rwParamsInMsgID, &clockTime, &readSize,
                    sizeof(RWArrayConfigFswMsg), &(ConfigData->rwConfigParams), moduleID);
    }

}

/*! This method takes the attitude and rate errors relative to the Reference frame, as well as
 the reference frame angular rates and acceleration, and computes the required control torque Lr.
 @return void
 @param ConfigData The configuration data associated with the MRP Steering attitude control
 @param callTime The clock time at which the function was called (nanoseconds)
 */

//*******************************************************************************//
//*******************************************************************************//
//*******************************************************************************//
/*
 Notes: AttGuideFswMsg contains arrays that are of size 3, quats are in size 4
 
 */
//*******************************************************************************//
//*******************************************************************************//
//*******************************************************************************//

void Update_B_DOT(B_DOTConfig *ConfigData, uint64_t callTime,
                  uint64_t moduleID)
{
    VehicleConfigFswMsg     sc;
    MagMeterIntMsg          magCmd;
    RWAvailabilityFswMsg    wheelsAvailability; /*!< Reaction wheel availability */
    RWSpeedIntMsg           wheelSpeeds;        /*!< Reaction wheel speed estimates */
    uint64_t                clockTime;
    uint32_t                readSize;

    float                   ctl_gain[8] = {ConfigData->K_detumble, 0.0, 0.0,0.0,0.0, 0.0,0.0,0.0};
    float                   out_u[3];
    double                  dbl_out_u[3];
    int                     i;
    float                   f_mag_bf[3];
    double                  Lr[3];
    
    
    /*! Begin method steps*/
    /*! - Read the input messages */
    ReadMessage(ConfigData->inputMagMeterID, &clockTime, &readSize,
                sizeof(MagMeterIntMsg), (void*) &(magCmd), moduleID);
    ReadMessage(ConfigData->inputVehicleConfigDataID, &clockTime, &readSize,
                sizeof(VehicleConfigFswMsg), (void*) &(sc), moduleID);


    memset(wheelSpeeds.wheelSpeeds, 0x0, MAX_EFF_CNT * sizeof(double));
    memset(wheelsAvailability.wheelAvailability, 0x0, MAX_EFF_CNT * sizeof(int)); // wheelAvailability set to 0 (AVAILABLE) by default
    if(ConfigData->rwConfigParams.numRW > 0) {
        ReadMessage(ConfigData->inputRWSpeedsID, &clockTime, &readSize,
                    sizeof(RWSpeedIntMsg), (void*) &(wheelSpeeds), moduleID);
        if (ConfigData->rwAvailInMsgID >= 0){
            ReadMessage(ConfigData->rwAvailInMsgID, &clockTime, &readSize,
                        sizeof(RWAvailabilityFswMsg), &wheelsAvailability, moduleID);
        }
    }

    for(i=0;i<3;i++){
        f_mag_bf[i] = magCmd.mag_bf[i];
    }

    ctl_bdot(f_mag_bf, ctl_gain, out_u);
    if(ConfigData->K_detumble==-0.0){
        dbl_out_u[0] = 0.0;
        dbl_out_u[1] = 0.0;
        dbl_out_u[2] = 0.0;
    }
    else{
        dbl_out_u[0] = out_u[0];
        dbl_out_u[1] = out_u[1];
        dbl_out_u[2] = out_u[2];
    }
    /*! - Store and write the output message */
    if (ConfigData->use_rw_wheels == 1){
        v3Cross(dbl_out_u,magCmd.mag_bf,Lr);
        v3Scale(1000,Lr,Lr);
        v3Copy(Lr, ConfigData->controlOut.torqueRequestBody);

        WriteMessage(ConfigData->outputMsgID, callTime, sizeof(CmdTorqueBodyIntMsg),
                 (void*) &(ConfigData->controlOut), moduleID);
    }
    else{
        v3Copy(dbl_out_u, ConfigData->controlOutTR.dipole_moment);

        WriteMessage(ConfigData->outputMsgID, callTime, sizeof(CmdTorqueRodsIntMsg),
                 (void*) &(ConfigData->controlOutTR), moduleID);
        }
    
    return;
}
// Add q_BR to input, will be the MRP to QUAT convert
void ctl_bdot(float *mag_bf, float *ctl_gain, float *out_u) {
    
    //    printf("%f %f %f\n", mag_bf[0], mag_bf[1], mag_bf[2]);
    int32_t i=0;
    static float mag_bf_prev[3] = {0.0,0.0,0.0};
    float mag_bf_rate[3];
    static uint32_t bdot_cnt = 1;
    
    // If previous mag data exists, take the derivative
    // Otherwise skip to next loop iteration
    if (mag_bf_prev[0] == 0.0 && mag_bf_prev[1] == 0.0 && mag_bf_prev[2] == 0.0){
        for (i=0;i<3;i++){
            mag_bf_prev[i] = mag_bf[i];
        }
    }
    else{
        // Calc Bdot
        for (i=0;i<3;i++){
            mag_bf_rate[i] = (mag_bf[i] - mag_bf_prev[i])/0.1;
            mag_bf_prev[i] = mag_bf[i];
//            out_u[i] = -1.0*ctl_gain[0]*mag_bf_rate[i]; // b-dot control law  TODO debug will

        }
        
        
        
        //        // Set control output at 1Hz
        if (bdot_cnt >= 10){
            for (i=0;i<3;i++){
                out_u[i] = -1.0*ctl_gain[0]*mag_bf_rate[i]; // b-dot control law  TODO debug will
            }
            bdot_cnt = 1;
        }else{
            bdot_cnt += 1;
            out_u[0] = 0.0;
            out_u[1] = 0.0;
            out_u[2] = 0.0;
        }
        
    }
}



