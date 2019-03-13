/*
 ISC License
 
 Copyright (c) 2016-2018, Autonomous Vehicle Systems Lab, University of Colorado at Boulder
 
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

#ifndef _MAXWELL_LS_H_
#define _MAXWELL_LS_H_

#include "messaging/static_messaging.h"
#include "simFswInterfaceMessages/navAttIntMsg.h"
#include "simFswInterfaceMessages/sunpointIntMsg.h"
#include "fswMessages/cssConfigFswMsg.h"
#include "fswMessages/cssUnitConfigFswMsg.h"
#include "simulation/utilities/mtx.h"
#include "simulation/utilities/conversions.h"
#include "simulation/utilities/types.h"
#include <stdint.h>
#include "simFswInterfaceMessages/cssArraySensorIntMsg.h"

/*! \addtogroup ADCSAlgGroup
 * @{
 */





/*! @brief Top level structure for the CSS weighted least squares estimator.
 Used to estimate the sun state in the vehicle body frame*/
typedef struct {
    float minUnitMag;   /*!< -- The minimally acceptable norm of sun body vector*/
    float smallAngle;   /*!< rad An angle value that specifies what is near 0 or 180 degrees */
    float eHat180_B;    /*!< -- Eigen axis to use if commanded axis is 180 from sun axis */
    float sunMnvrVec[3];
    char cssDataInMsgName[MAX_STAT_MSG_LENGTH]; /*!< The name of the css sensor input message*/
    char cssConfigInMsgName[MAX_STAT_MSG_LENGTH]; /*!< The name of the css configuration input message*/
    char navStateOutMsgName[MAX_STAT_MSG_LENGTH]; /*!< The name of the navigation output message*/
    char sunpointOutMsgName[MAX_STAT_MSG_LENGTH];
    uint32_t numActiveCss;   /*!< -- Number of currently active CSS sensors*/
    double sensorUseThresh;  /*!< -- Threshold below which we discount sensors*/
    CSSConfigFswMsg cssConfigInBuffer; /*!< -- CSS constellation configuration message buffer */
    NavAttIntMsg sunlineOutBuffer; /*!< -- Nav message*/
    sunpointIntMsg sunDirection;
    int32_t sunpointOutMsgID;
    int32_t cssDataInMsgID;      /*!< -- ID for the incoming CSS sensor message*/
    int32_t cssConfigInMsgID;      /*!< -- ID for the incoming CSS configuration message*/
    int32_t navStateOutMsgId;     /*!< -- ID for the outgoing body estimate message*/
}maxwellLSConfig;

#ifdef __cplusplus
extern "C" {
#endif
    
    void SelfInit_maxwellLS(maxwellLSConfig *ConfigData, uint64_t moduleID);
    void CrossInit_maxwellLS(maxwellLSConfig *ConfigData, uint64_t moduleID);
    void Update_maxwellLS(maxwellLSConfig *ConfigData, uint64_t callTime,
                          uint64_t moduleID);
    void Reset_maxwellLS(maxwellLSConfig *ConfigData, uint64_t callTime, uint64_t moduleID);
    void cal_sun_sens(struct mtx_matrix *sun_sens_volt, struct mtx_matrix *sun_sens_bfmtx,
                  struct mtx_matrix *sun_sens_cal_bfmtx, float ss_v_cutoff);
    void create_qBR(float *sun_vec, float *qBR, float *sHatBdyCmd);
    void compute_LS(int num_active_css, float *sun_sens_map, float *y, float x[3]);

    
#ifdef __cplusplus
}
#endif

/*! @} */

#endif
