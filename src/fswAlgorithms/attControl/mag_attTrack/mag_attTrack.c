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
 mag_attTrack Module
 
 */

#include "attControl/mag_attTrack/mag_attTrack.h"
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
void SelfInit_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t moduleID)
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
void CrossInit_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t moduleID)
{
    /*! - Get the control data message IDs*/
    ConfigData->vehConfigInMsgID = subscribeToMessage(ConfigData->vehConfigInMsgName,
                                                      sizeof(VehicleConfigFswMsg), moduleID);
    ConfigData->inputMagMeterID = subscribeToMessage(ConfigData->inputMagMeterName,
                                                     sizeof(MagMeterIntMsg), moduleID);
    
    /*! - Get the Guidance Message */
    ConfigData->inputGuidID = subscribeToMessage(ConfigData->inputGuidName,
                                                 sizeof(AttGuidFswMsg), moduleID);
    


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
void Reset_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t callTime, uint64_t moduleID)
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

void Update_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t callTime,
                  uint64_t moduleID)
{
    AttGuidFswMsg           guidCmd;
    VehicleConfigFswMsg     sc;
    MagMeterIntMsg          magCmd;
    RWAvailabilityFswMsg    wheelsAvailability; /*!< Reaction wheel availability */
    RWSpeedIntMsg           wheelSpeeds;        /*!< Reaction wheel speed estimates */
    uint64_t                clockTime;
    uint32_t                readSize;

    double                  ctl_gain[8] = {ConfigData->K_sigma, ConfigData->K_omega, 0.0,0.0,0.0, 0.0,0.0,0.0};
    double                  out_m[3];  // Commanded Dipople moment vector
    double                  Lr[3];
    // Define rate and MRP attitude errors for law
    double                  omega_BN_B[3];
    
    
    /*! Begin method steps*/
    /*! - Read the input messages */
    ReadMessage(ConfigData->inputMagMeterID, &clockTime, &readSize,
                sizeof(MagMeterIntMsg), (void*) &(magCmd), moduleID);
    ReadMessage(ConfigData->inputVehicleConfigDataID, &clockTime, &readSize,
                sizeof(VehicleConfigFswMsg), (void*) &(sc), moduleID);
    ReadMessage(ConfigData->inputGuidID, &clockTime, &readSize,
                sizeof(AttGuidFswMsg), (void*) &(guidCmd), moduleID);


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
    
    /* compute body rate */
    v3Add(guidCmd.omega_BR_B, guidCmd.omega_RN_B, omega_BN_B);

    // Run control law
    if(ConfigData->K_sigma==0.0){
        for (int i = 0; i < 3; i++) {
            out_m[i] = 0.0;
        }
    } else {
        ctl_mag_att_track(magCmd.mag_bf, ctl_gain, out_m, guidCmd.sigma_BR, guidCmd.omega_BR_B, guidCmd.omega_RN_B, guidCmd.domega_RN_B, omega_BN_B, sc.ISCPntB_B);
    }
    
    /*! - Store and write the output message */
    if (ConfigData->use_rw_wheels == 1){
        v3Cross(out_m,magCmd.mag_bf,Lr);
        v3Scale(1000,Lr,Lr);
        v3Copy(Lr, ConfigData->controlOut.torqueRequestBody);

        WriteMessage(ConfigData->outputMsgID, callTime, sizeof(CmdTorqueBodyIntMsg),
                 (void*) &(ConfigData->controlOut), moduleID);
    }
    else{
        v3Copy(out_m, ConfigData->controlOutTR.dipole_moment);
        
        WriteMessage(ConfigData->outputMsgID, callTime, sizeof(CmdTorqueRodsIntMsg),
                     (void*) &(ConfigData->controlOutTR), moduleID);
    }
    
    return;
}

/* Use control law from equation 8.84 in Schaub's book (Chapter 8.4, nonlinear control) but excludes the torque 'L' Term */
void ctl_mag_att_track(double *mag_bf, double *ctl_gain, double *out_m, double *sigma_BR, double *omega_BR_B, double *omega_RN_B, double *domega_RN_B, double *omega_BN_B, double *I)
{
    // Get Gains
    double K_s = ctl_gain[0];
    double K_w = ctl_gain[1];
    double ks_times_sigma[3];
    double kw_times_delomega_r[3];
    double domega_r_minus_omega_cross_omega_r[3];
    double omega_r_cross_I_omega[3];
    double mag_norm;
    double sq = 2.0;
    size_t dim_I = 3;

    // magnetic field norm
    mag_norm = v3Norm(mag_bf);
    // K times sigma
    v3Scale(K_s, sigma_BR, ks_times_sigma);
    // K times omega minus omega_r
    v3Subtract(omega_BN_B, omega_RN_B, kw_times_delomega_r);
    v3Scale(K_w, kw_times_delomega_r, kw_times_delomega_r);
    // domega_r minus omega times omega_r
    v3Cross(omega_BN_B, omega_RN_B, domega_r_minus_omega_cross_omega_r);
    v3Subtract(domega_RN_B, domega_r_minus_omega_cross_omega_r, domega_r_minus_omega_cross_omega_r);
    mMultV(I, dim_I, dim_I, domega_r_minus_omega_cross_omega_r, domega_r_minus_omega_cross_omega_r);
    // omega_r cross I omega
    mMultV(I, dim_I, dim_I, omega_BN_B, omega_r_cross_I_omega);
    v3Cross(omega_RN_B, omega_r_cross_I_omega, omega_r_cross_I_omega);
    
    // Compute total law
    v3Add(ks_times_sigma, kw_times_delomega_r, out_m);
    v3Subtract(out_m, domega_r_minus_omega_cross_omega_r, out_m);
    v3Subtract(out_m, omega_r_cross_I_omega, out_m);
    
    // Now compute commanded dipole
    v3Cross(out_m, mag_bf, out_m);
    v3Scale(1.0/pow(mag_norm, sq), out_m, out_m);
    v3Add(out_m, mag_bf, out_m);
    
}