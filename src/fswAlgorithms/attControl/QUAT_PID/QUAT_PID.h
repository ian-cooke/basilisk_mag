/*
 ISC License

 Copyright (c) 2016, Autonomous Vehicle Systems Lab, University of Colorado at Boulder

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

#ifndef _QUAT_PID_CONTROL_H_
#define _QUAT_PID_CONTROL_H_

#include "messaging/static_messaging.h"
#include "fswMessages/attGuidFswMsg.h"
#include "fswMessages/vehicleConfigFswMsg.h"
#include "fswMessages/rwArrayConfigFswMsg.h"
#include "simFswInterfaceMessages/rwSpeedIntMsg.h"
#include "simFswInterfaceMessages/cmdTorqueBodyIntMsg.h"
#include "simFswInterfaceMessages/imuSensorIntMsg.h"
#include "simFswInterfaceMessages/sunpointIntMsg.h"
#include "simFswInterfaceMessages/navAttIntMsg.h"
#include "simulation/utilities/mtx.h"
#include "fswMessages/quatGuidFswMsg.h"

#include <stdint.h>

/*! \addtogroup ADCSAlgGroup
 * @{
 */

/*!@brief Data structure for the MRP feedback attitude control routine.

 The module
 [PDF Description](AVS-Sim-MRP_Feedback-2016-0108.pdf)
 contains further information on this module's function,
 how to run it, as well as testing.
 */


typedef struct {
    /* declare module private variables */
    double K;
    double P;
    double K_I;
    double ISCPntB_B[9];                /*!< [kg m^2] Spacecraft Inertia */
    RWArrayConfigFswMsg rwConfigParams;      /*!< [-] struct to store message containing RW config parameters in body B frame */
    uint64_t priorTime;


    /* declare module IO interfaces */
    char rwParamsInMsgName[MAX_STAT_MSG_LENGTH];        /*!< The name of the RWArrayConfigFswMsg input message*/
    int32_t rwParamsInMsgID;                            /*!< [-] ID for the RWArrayConfigFswMsg ingoing message */
    char vehConfigInMsgName[MAX_STAT_MSG_LENGTH];
    int32_t vehConfigInMsgID;
    char rwAvailInMsgName[MAX_STAT_MSG_LENGTH];         /*!< [-] The name of the RWs availability message*/
    int32_t rwAvailInMsgID;                             /*!< [-] ID for the incoming  RWs availability data*/


    char outputErrorName[MAX_STAT_MSG_LENGTH];
    char outputDataName[MAX_STAT_MSG_LENGTH];           /*!< [-] The name of the output message*/
    char inputGuidName[MAX_STAT_MSG_LENGTH];            /*!< [-] The name of the Input message*/
    char inputAttName[MAX_STAT_MSG_LENGTH];
    char inputRatesName[MAX_STAT_MSG_LENGTH];
    char inputSunName[MAX_STAT_MSG_LENGTH];
    char inputRWSpeedsName[MAX_STAT_MSG_LENGTH];        /*!< [-] The name for the reaction wheel speeds message */
    int32_t inputRWSpeedsID;                            /*!< [-] ID for the reaction wheel speeds message*/
    int32_t outputMsgID;                                /*!< [-] ID for the outgoing body accel requests*/
    int32_t outputErrorID;
    int32_t inputGuidID;                                /*!< [-] ID for the incoming guidance errors*/
    int32_t inputAttID;
    int32_t inputRatesID;
    int32_t inputSunID;

    CmdTorqueBodyIntMsg controlOut;                    /*!< -- Control output requests */
    QuatGuidFswMsg controlError;

}QUAT_PIDConfig;

#ifdef __cplusplus
extern "C" {
#endif
    
    void SelfInit_QUAT_PID(QUAT_PIDConfig *ConfigData, uint64_t moduleID);
    void CrossInit_QUAT_PID(QUAT_PIDConfig *ConfigData, uint64_t moduleID);
    void Update_QUAT_PID(QUAT_PIDConfig *ConfigData, uint64_t callTime, uint64_t moduleID);
    void Reset_QUAT_PID(QUAT_PIDConfig *ConfigData, uint64_t callTime, uint64_t moduleID);
    void ctl_pid(float *q_BR, float *omega_BN, float *omega_RN, float *omega_BR, float *domega_RN, float *ctl_gain, float *I_RW_values, float *rw_spin_rates, float *GsValues, float *JsValues, float *out_u);
    void calc_q_error(float *q_bn, float *q_rn, float *q_br);
    void q_2_dcm(struct mtx_matrix* q, struct mtx_matrix* dcm);
    void dcm_2_q(struct mtx_matrix* dcm, struct mtx_matrix* q);

#ifdef __cplusplus
}
#endif

/*! @} */

#endif
