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

#ifndef _mag_ATT_TRACK_CONTROL_H_
#define _mag_ATT_TRACK_CONTROL_H_

#include "messaging/static_messaging.h"
#include "fswMessages/attGuidFswMsg.h"
#include "fswMessages/vehicleConfigFswMsg.h"
#include "simFswInterfaceMessages/MagMeterIntMsg.h"
#include "simFswInterfaceMessages/cmdTorqueBodyIntMsg.h"
#include "simFswInterfaceMessages/cmdTorqueRodsIntMsg.h"
#include "simulation/utilities/types.h"
#include "fswMessages/rwArrayConfigFswMsg.h"
#include "simFswInterfaceMessages/rwSpeedIntMsg.h"
#include "simFswInterfaceMessages/navAttIntMsg.h"



#include <stdint.h>


/*! @brief Top level structure for the QUAT Steering attitude control routine. */
typedef struct {
    /* declare module private variables */
    double K_sigma;                           /*!< Proportional gain applied to MRP attitude errors */
    double K_omega;                           /*!< Derivative gain applied to angular rate errors */
    float use_rw_wheels;
    double knownTorquePntB_B[3];        /*!< [N*m]     known external torque in body frame vector components */
    int controlLaw;
    
    
    /* declare module IO interfaces */
    char vehConfigInMsgName[MAX_STAT_MSG_LENGTH];
    int32_t vehConfigInMsgID;
    char rwParamsInMsgName[MAX_STAT_MSG_LENGTH];        /*!< The name of the RWArrayConfigFswMsg input message*/
    int32_t rwParamsInMsgID;                            /*!< [-] ID for the RWArrayConfigFswMsg ingoing message */
    char rwAvailInMsgName[MAX_STAT_MSG_LENGTH];         /*!< [-] The name of the RWs availability message*/
    int32_t rwAvailInMsgID;                             /*!< [-] ID for the incoming  RWs availability data*/
    char inputGuidName[MAX_STAT_MSG_LENGTH];            /*!< [-] The name of the Input message*/
    int32_t inputGuidID;                                /*!< [-] ID for the incoming guidance errors*/
    char inputNavAttName[MAX_STAT_MSG_LENGTH];
    int32_t inputNavAttID;

    /* declare module IO interfaces */                      /*!< [-] ID for the incoming  RWs availability data*/
    char outputDataName[MAX_STAT_MSG_LENGTH];             /*!< The name of the output message*/
    char inputMagMeterName[MAX_STAT_MSG_LENGTH];
    char inputVehicleConfigDataName[MAX_STAT_MSG_LENGTH];   /*!< The name of the Input message*/
    char inputRWSpeedsName[MAX_STAT_MSG_LENGTH];            /*!< [-] The name for the reaction wheel speeds message */
    int32_t inputRWSpeedsID;                                /*!< [-] ID for the reaction wheel speeds message*/
    int32_t inputMagMeterID;
    int32_t outputMsgID;                                  /*!< [] ID for the outgoing body accel requests*/
    int32_t inputVehicleConfigDataID;                       /*!< [] ID for the incoming static vehicle data */
    CmdTorqueRodsIntMsg controlOutTR;                         /*!< [] Control output requests */
    CmdTorqueBodyIntMsg controlOut;                       /*!< [] Control output requests */
    RWArrayConfigFswMsg rwConfigParams;                     /*!< [-] struct to store message containing RW config parameters in body B frame */

    
}mag_attTrackConfig;

#ifdef __cplusplus
extern "C" {
#endif
    
    void SelfInit_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t moduleID);
    void CrossInit_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t moduleID);
    void Update_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t callTime, uint64_t moduleID);
    void Reset_mag_attTrack(mag_attTrackConfig *ConfigData, uint64_t callTime, uint64_t moduleID);
    void ctl_mag_att_track_one(double *mag_bf, double *ctl_gain, double *out_m, double *sigma_BR, double *omega_BR_B, double *omega_RN_B, double *domega_RN_B, double *omega_BN_B, double *I);
    void ctl_mag_att_track_two(double *mag_bf, double *ctl_gain, double *out_m, double *sigma_BR, double *omega_BN_B);
    void ctl_mag_att_track_three(double *mag_bf, double *ctl_gain, double *out_m, double *omega_BN_B);
    void ctl_mag_att_track_four(double *mag_bf, double *ctl_gain, double *out_m);
#ifdef __cplusplus
}
#endif

/*! @} */

#endif
