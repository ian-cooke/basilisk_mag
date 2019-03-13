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
/*
    QUAT_PD Module
 
 */

#include "attControl/QUAT_PD/QUAT_PD.h"
#include "simulation/utilities/linearAlgebra.h"
#include "simulation/utilities/rigidBodyKinematics.h"
#include "simFswInterfaceMessages/macroDefinitions.h"
#include "simulation/utilities/astroConstants.h"
#include "fswMessages/rwAvailabilityFswMsg.h"
#include "simulation/utilities/bsk_Print.h"
#include "fswMessages/quatGuidFswMsg.h"


#include <string.h>
#include <math.h>
#include<stdlib.h>

/*! This method initializes the ConfigData for this module.
 It checks to ensure that the inputs are sane and then creates the
 output message
 @return void
 @param ConfigData The configuration data associated with this module
 */
void SelfInit_QUAT_PD(QUAT_PDConfig *ConfigData, uint64_t moduleID)
{
    
    /*! Begin method steps */
    /*! - Create output message for module */
    ConfigData->outputErrorID = CreateNewMessage(ConfigData->outputErrorName,
        sizeof(QuatGuidFswMsg), "QuatGuidFswMsg", moduleID);

    ConfigData->outputMsgID = CreateNewMessage(ConfigData->outputDataName,
        sizeof(CmdTorqueBodyIntMsg), "CmdTorqueBodyIntMsg", moduleID);



    
}

/*! This method performs the second stage of initialization for this module.
 It's primary function is to link the input messages that were created elsewhere.
 @return void
 @param ConfigData The configuration data associated with this module
 */
void CrossInit_QUAT_PD(QUAT_PDConfig *ConfigData, uint64_t moduleID)
{
    /*! - Get the control data message ID*/
    ConfigData->inputGuidID = subscribeToMessage(ConfigData->inputGuidName,
                                                 sizeof(AttGuidFswMsg), moduleID);
    ConfigData->inputAttID = subscribeToMessage(ConfigData->inputAttName,
                                                 sizeof(NavAttIntMsg), moduleID);
    ConfigData->inputRatesID = subscribeToMessage(ConfigData->inputRatesName,
                                                 sizeof(IMUSensorIntMsg), moduleID);
    ConfigData->inputSunID = subscribeToMessage(ConfigData->inputSunName,
                                                 sizeof(sunpointIntMsg), moduleID);

    ConfigData->vehConfigInMsgID = subscribeToMessage(ConfigData->vehConfigInMsgName,
                                                 sizeof(VehicleConfigFswMsg), moduleID);

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
void Reset_QUAT_PD(QUAT_PDConfig *ConfigData, uint64_t callTime, uint64_t moduleID)
{
    /*! - Read the input messages */
    uint64_t clockTime;
    uint32_t readSize;
    int i;

    VehicleConfigFswMsg sc;
    ReadMessage(ConfigData->vehConfigInMsgID, &clockTime, &readSize,
                sizeof(VehicleConfigFswMsg), (void*) &(sc), moduleID);
    for (i=0; i < 9; i++){
        ConfigData->ISCPntB_B[i] = sc.ISCPntB_B[i];
    };

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
void Update_QUAT_PD(QUAT_PDConfig *ConfigData, uint64_t callTime,
    uint64_t moduleID)
{
    AttGuidFswMsg           guidCmd;            /*!< Guidance Message */
	NavAttIntMsg            attitude;
    IMUSensorIntMsg         rates;
    sunpointIntMsg          sunDirection;
    RWSpeedIntMsg           wheelSpeeds;        /*!< Reaction wheel speed estimates */
    RWAvailabilityFswMsg    wheelsAvailability; /*!< Reaction wheel availability */
    VehicleConfigFswMsg     sc;
    uint64_t            clockTime;
    uint32_t            readSize;

    int             i;
    double          q_BR[4];
    float           q_BRf[4];
    double          q_BN[4];
    double          omega_BN[3];
    float           omega_BNf[3];
    float           omega_RNf[3] = {0.0,0.0,0.0};
    float           omega_BRf[3];
    float           domega_RNf[3] = {0.0,0.0,0.0};

    float           ctl_gain[8] = {0.0, ConfigData->K, ConfigData->P, ConfigData->P,ConfigData->P,
                                        0.0,0.0,0.0};
    double          Lr[3];              /*!< required control torque vector [Nm] */
    float           I_RW_values[9] = {ConfigData->ISCPntB_B[0],0.0,0.0, 0.0,ConfigData->ISCPntB_B[4],0.0, 0.0,0.0,ConfigData->ISCPntB_B[8]};
    float           GsValues[12] = {0.422618261740699, 0.422618261740699, 0.422618261740699, 0.422618261740699,
                                    0.906307787036650, 0.0, -0.906307787036650,  0.0,
                                     0.0, 0.906307787036650, 0.0, -0.906307787036650};
    float           out_u[3];
    float           JsValues[4];
    double          Gshs[3];
    float           Gshsf[3];
    double           *wheelGs;


    /*! Begin method steps*/
    /*! - Read the dynamic input messages */
    memset(&guidCmd, 0x0, sizeof(AttGuidFswMsg));
    memset(&attitude, 0x0, sizeof(NavAttIntMsg));
    memset(&rates, 0x0, sizeof(IMUSensorIntMsg));
    memset(&sunDirection, 0x0, sizeof(sunpointIntMsg));

    ReadMessage(ConfigData->inputGuidID, &clockTime, &readSize,
                sizeof(AttGuidFswMsg), (void*) &(guidCmd), moduleID);
    ReadMessage(ConfigData->inputAttID, &clockTime, &readSize,
                sizeof(NavAttIntMsg), (void*) &(attitude), moduleID);
    ReadMessage(ConfigData->inputRatesID, &clockTime, &readSize,
                sizeof(IMUSensorIntMsg), (void*) &(rates), moduleID);
    ReadMessage(ConfigData->inputSunID, &clockTime, &readSize,
                sizeof(sunpointIntMsg), (void*) &(sunDirection), moduleID);

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

    ////////////////////* START QUAT PD CODE*////////////////////////////
    /* Get True Attitude: TODO: replace with Star Tracker Measurement */
    MRP2EP(attitude.sigma_BN,q_BN);

    /* double to float conversion for angular rate */
    for (i=0;i<3;i++){
        omega_BNf[i] = rates.AngVelPlatform[i];
        omega_RNf[i] = guidCmd.omega_RN_B[i];
        omega_BRf[i] = guidCmd.omega_BR_B[i]; /* omega RN = 0.0 */
        domega_RNf[i] = guidCmd.domega_RN_B[i];
    }

    /* double to float conversion for attitude error */
    MRP2EP(guidCmd.sigma_BR, q_BR);
    for (i=0;i<4;i++) {
        q_BRf[i] = q_BR[i];
    }

////    /*********** LEAST SQUARES FOR RATE GYRO *****************/
//    static int count = 0;
//    static float xkm1[3];
//    static float xk[3];
//    static float Kk[9] = {0.9,0.0,0.0, 0.0,0.9,0.0, 0.0,0.0,0.9};
//    static float Pk[9] = {1000.0,0.0,0.0, 0.0,1000.0,0.0, 0.0,0.0,1000.0};
//    static float Pkm1[9];
//    float yk[3];
//
//    struct mtx_matrix Kk_mtx;
//    struct mtx_matrix Hk_mtx;
//    struct mtx_matrix Pkm1_mtx;
//    struct mtx_matrix Rk_mtx;
//    struct mtx_matrix II;
//    struct mtx_matrix tmp_33a;
//    struct mtx_matrix tmp_33b;
//    struct mtx_matrix tmp_31a;
//    struct mtx_matrix xk_mtx;
//    struct mtx_matrix xkm1_mtx;
//    struct mtx_matrix Pk_mtx;
//    struct mtx_matrix yk_mtx;
//
//    mtx_create_eye(3,3,&II);
//    mtx_create_eye(3,3,&Hk_mtx);
//    mtx_create_eye(3,3,&Rk_mtx);
//    mtx_create_ones(3,3,&tmp_33a);
//    mtx_create_ones(3,3,&tmp_33b);
//    mtx_create_ones(3,3,&xk_mtx);
//    mtx_create_ones(3,1,&tmp_31a);
//
//
//
//    if (count == 0) {
//        xkm1[0] = omega_BNf[0];
//        xkm1[1] = omega_BNf[1];
//        xkm1[2] = omega_BNf[2];
//        for (i=0;i<9;i++){
//            Pkm1[i] = Pk[i];
//        }
//        count ++;
//    } else {
//        yk[0] = omega_BNf[0];
//        yk[1] = omega_BNf[1];
//        yk[2] = omega_BNf[2];
//        mtx_create(3,1,yk,&yk_mtx);
//        mtx_create_ones(3,3,&Kk_mtx);
//        mtx_create(3,3,Pkm1,&Pkm1_mtx);
//
//        /* Kk = Pkm1 (Pkm1 + Rk)^-1  */
//        mtx_sum(&Pkm1_mtx,&Rk_mtx,&tmp_33a);
//        mtx_inv(&tmp_33a,&tmp_33a);
//        mtx_mult(&Pkm1_mtx,&tmp_33a,&Kk_mtx);
//
//
//        mtx_create(3,1,xkm1,&xkm1_mtx);
//        mtx_mult(&Hk_mtx,&xkm1_mtx,&tmp_31a);
//        mtx_scale(&tmp_31a,-1.0,&tmp_31a);
//        mtx_sum(&yk_mtx,&tmp_31a,&tmp_31a);
//        mtx_mult(&Kk_mtx,&tmp_31a,&tmp_31a);
//        mtx_sum(&xkm1_mtx,&tmp_31a,&xk_mtx); /* RATE GYRO FILTERED */
//
//        mtx_scale(&Kk_mtx,-1.0,&tmp_33a);
//        mtx_sum(&II,&tmp_33a,&tmp_33a); /* I - Kk */
//        mtx_trans(&tmp_33a,&tmp_33b); /* (I - Kk)^T */
//        mtx_mult(&tmp_33a,&Pkm1_mtx,&tmp_33a);
//        mtx_mult(&tmp_33a,&tmp_33b,&tmp_33a);
//
//        mtx_trans(&Kk_mtx,&tmp_33b);
//        mtx_mult(&Kk_mtx,&tmp_33b,&tmp_33b);
//        mtx_sum(&tmp_33a,&tmp_33b,&Pk_mtx);
//
//        Pkm1[0] = mtx_get(1,1,&Pk_mtx);
//        Pkm1[1] = mtx_get(1,2,&Pk_mtx);
//        Pkm1[2] = mtx_get(1,3,&Pk_mtx);
//
//        Pkm1[3] = mtx_get(2,1,&Pk_mtx);
//        Pkm1[4] = mtx_get(2,2,&Pk_mtx);
//        Pkm1[5] = mtx_get(2,3,&Pk_mtx);
//
//        Pkm1[6] = mtx_get(3,1,&Pk_mtx);
//        Pkm1[7] = mtx_get(3,2,&Pk_mtx);
//        Pkm1[8] = mtx_get(3,3,&Pk_mtx);
//
//        /* Store Previous estimate */
//        for (i=0;i<3;i++) {
//            xkm1[i] = mtx_get(i+1,1,&xk_mtx);
//        }
//
//        count ++;
//    }
//
//    omega_BNf[0] = mtx_get(1,1,&xk_mtx);
//    omega_BNf[1] = mtx_get(2,1,&xk_mtx);
//    omega_BNf[2] = mtx_get(3,1,&xk_mtx);

/****************************************************************/



//    /* Reaction Wheel rates and values */
    float rw_spin_rates[4] = {0.0,0.0,0.0,0.0};

    for(i = 0; i < ConfigData->rwConfigParams.numRW; i++)
    {
        if (wheelsAvailability.wheelAvailability[i] == AVAILABLE){ /* check if wheel is available */
            rw_spin_rates[i] = wheelSpeeds.wheelSpeeds[i];
            JsValues[i] = ConfigData->rwConfigParams.JsList[i];
            wheelGs = &(ConfigData->rwConfigParams.GsMatrix_B[i*3]);
            v3Scale(ConfigData->rwConfigParams.JsList[i] * (v3Dot(omega_BN, wheelGs) + wheelSpeeds.wheelSpeeds[i]),
                    wheelGs, Gshs);
        }
    }

    for (i=0;i<3;i++){
        Gshsf[i] = Gshs[i];
        }


    ctl_pd(q_BRf, omega_BNf, omega_RNf, omega_BRf, domega_RNf, ctl_gain, I_RW_values, rw_spin_rates, GsValues, JsValues, out_u);
    for (i=0;i<3;i++) {
        Lr[i] = out_u[i];
    }


/* store the output message */

    v3Copy(Lr, ConfigData->controlOut.torqueRequestBody);
    for(i=0;i<4;i++){
        q_BR[i]=q_BRf[i];
    }
    EP2MRP(q_BR,ConfigData->controlError.sigma_BR);
//    v4Copy(q_BR, ConfigData->controlError.q_BR);

    WriteMessage(ConfigData->outputMsgID, callTime, sizeof(CmdTorqueBodyIntMsg),
                 (void*) &(ConfigData->controlOut), moduleID);

    WriteMessage(ConfigData->outputErrorID, callTime, sizeof(QuatGuidFswMsg),
                 (void*) &(ConfigData->controlError), moduleID);


    return;
}
void ctl_pd(float *q_BR, float *omega_BN, float *omega_RN, float *omega_BR, float *domega_RN, float *ctl_gain, float *I_RW_values, float *rw_spin_rates, float *GsValues, float *JsValues, float *out_u) {

    int32_t i;
    int32_t rv;
    struct mtx_matrix I_RW;
    struct mtx_matrix Gs_mtx;
    struct mtx_matrix hs_mtx;
    struct mtx_matrix gs1m;
    struct mtx_matrix gs2m;
    struct mtx_matrix gs3m;
    struct mtx_matrix gs4m;
    struct mtx_matrix g_omega;
    struct mtx_matrix tmp_31a;
    struct mtx_matrix tmp_31b;
    struct mtx_matrix tmp_33a;
    struct mtx_matrix tmp_33b;
    struct mtx_matrix out_u_mtx;
    mtx_create(3,3,I_RW_values, &I_RW);
    mtx_create_val(3,1,&out_u_mtx,0.0);

    mtx_create_ones(3,3,&tmp_33a);

    float EP_BR[3];
    float h1;
    float h2;
    float h3;
    float h4;
    float gs1[3] = {0.422618261740699,0.906307787036650,0.0};
    float gs2[3] = {0.422618261740699,0.0,0.906307787036650};
    float gs3[3] = {0.422618261740699,-0.906307787036650,0.0};
    float gs4[3] = {0.422618261740699,0.0,-0.906307787036650};

    for (i=0;i<3;i++){
        EP_BR[i] = q_BR[i+1];
    }

    /******  -K * Epsilon_BR ******/
    mtx_create(3,1,EP_BR,&tmp_31a);
    mtx_scale(&tmp_31a,-1.0*ctl_gain[1],&tmp_31a);
    mtx_sum(&out_u_mtx,&tmp_31a,&out_u_mtx);

    /****** -P * delta_omega ******/
    mtx_create(3,1,omega_BR,&tmp_31b);
    mtx_scale(&tmp_31b, -1.0*ctl_gain[2],&tmp_31b);
    mtx_sum(&out_u_mtx,&tmp_31b,&out_u_mtx);

    /****** [I](domega_RN - omega_BR x omega_RN ******/
    mtx_create(3,1,omega_BN,&tmp_31a);
    mtx_ss(&tmp_31a,&tmp_33a);
    mtx_create(3,1,omega_RN,&tmp_31b);
    mtx_mult(&tmp_33a,&tmp_31b,&tmp_31a);
    mtx_create(3,1,domega_RN,&tmp_31b);
    mtx_scale(&tmp_31a,-1.0,&tmp_31a);
    mtx_sum(&tmp_31b,&tmp_31a,&tmp_31a);
    mtx_mult(&I_RW,&tmp_31a,&tmp_31a);
    mtx_sum(&out_u_mtx,&tmp_31a,&out_u_mtx);

    /****** +omega x [I]omega ******/
    mtx_create(3,1,omega_BN,&tmp_31a);
    mtx_mult(&I_RW, &tmp_31a, &tmp_31b);
    mtx_ss(&tmp_31a,&tmp_33a);
    mtx_mult(&tmp_33a,&tmp_31b,&tmp_31b);
    mtx_sum(&out_u_mtx,&tmp_31b,&out_u_mtx);

    /* h_i = J_si * (Omega_i + g_si^T * omega) */
    mtx_create(3,4,GsValues,&Gs_mtx);
    mtx_create_val(4,1,&hs_mtx,0.0);
    mtx_create(1,3,gs1,&gs1m);
    mtx_create(1,3,gs2,&gs2m);
    mtx_create(1,3,gs3,&gs3m);
    mtx_create(1,3,gs4,&gs4m);
    mtx_create(3,1,omega_BN,&tmp_31a);
    mtx_ss(&tmp_31a,&tmp_33a);
    mtx_create_val(1,1,&g_omega,0.0);

    mtx_mult(&gs1m,&tmp_31a,&g_omega);
    h1 = JsValues[0]*(rw_spin_rates[0] + mtx_get(1,1,&g_omega));

    mtx_mult(&gs2m,&tmp_31a,&g_omega);
    h2 = JsValues[1]*(rw_spin_rates[1] + mtx_get(1,1,&g_omega));

    mtx_mult(&gs3m,&tmp_31a,&g_omega);
    h3 = JsValues[2]*(rw_spin_rates[2] + mtx_get(1,1,&g_omega));

    mtx_mult(&gs4m,&tmp_31a,&g_omega);
    h4 = JsValues[3]*(rw_spin_rates[3] + mtx_get(1,1,&g_omega));

    float hs[4] = {h1,h2,h3,h4};

    /****** omega_BN x [Gs]hs ******/
    mtx_create(4,1,hs,&hs_mtx);
    mtx_mult(&Gs_mtx,&hs_mtx,&tmp_31a);
    mtx_mult(&tmp_33a,&tmp_31a,&tmp_31a);
    mtx_sum(&out_u_mtx,&tmp_31a,&out_u_mtx);


    for (i=0;i<3;i++){
        out_u[i] = mtx_get(i+1,1,&out_u_mtx);
    }
    return;

}

void calc_q_error(float *q_bn, float *q_rn, float *q_br){


    struct mtx_matrix dcm_BN;
    struct mtx_matrix dcm_RN;
    struct mtx_matrix dcm_NR;
    struct mtx_matrix dcm_BR;
    struct mtx_matrix q_BN;
    struct mtx_matrix q_RN;
    struct mtx_matrix q_BR;

    mtx_create_val(3,3,&dcm_BN,0);
    mtx_create_val(3,3,&dcm_RN,0);
    mtx_create_val(3,3,&dcm_NR,0);
    mtx_create_val(3,3,&dcm_BR,0);
    mtx_create_val(4,1,&q_BR,0);
    mtx_create(4,1,q_bn,&q_BN);
    mtx_create(4,1,q_rn,&q_RN);
    q_2_dcm(&q_BN,&dcm_BN);
    q_2_dcm(&q_RN,&dcm_RN);

    mtx_trans(&dcm_RN,&dcm_NR);
    mtx_mult(&dcm_BN,&dcm_NR,&dcm_BR);


    dcm_2_q(&dcm_BR,&q_BR);
    q_br[0] = mtx_get(1,1,&q_BR);
    q_br[1] = mtx_get(2,1,&q_BR);
    q_br[2] = mtx_get(3,1,&q_BR);
    q_br[3] = mtx_get(4,1,&q_BR);



}

void q_2_dcm(struct mtx_matrix* q, struct mtx_matrix* dcm) {

	mtx_set(1, 1, dcm,
		mtx_get(1, 1, q)*mtx_get(1, 1, q)
		+ mtx_get(2, 1, q)*mtx_get(2, 1, q)
		- mtx_get(3, 1, q)*mtx_get(3, 1, q)
		- mtx_get(4, 1, q)*mtx_get(4, 1, q));

	mtx_set(1, 2, dcm,
		2 * (mtx_get(2, 1, q)*mtx_get(3, 1, q) + mtx_get(1, 1, q)*mtx_get(4, 1, q)));

	mtx_set(1, 3, dcm,
		2 * (mtx_get(2, 1, q)*mtx_get(4, 1, q) - mtx_get(1, 1, q)*mtx_get(3, 1, q)));

	mtx_set(2, 1, dcm,
		2 * (mtx_get(2, 1, q)*mtx_get(3, 1, q) - mtx_get(1, 1, q)*mtx_get(4, 1, q)));

	mtx_set(2, 2, dcm,
		mtx_get(1, 1, q)*mtx_get(1, 1, q)
		- mtx_get(2, 1, q)*mtx_get(2, 1, q)
		+ mtx_get(3, 1, q)*mtx_get(3, 1, q)
		- mtx_get(4, 1, q)*mtx_get(4, 1, q));

	mtx_set(2, 3, dcm,
		2 * (mtx_get(3, 1, q)*mtx_get(4, 1, q) + mtx_get(1, 1, q)*mtx_get(2, 1, q)));

	mtx_set(3, 1, dcm,
		2 * (mtx_get(2, 1, q)*mtx_get(4, 1, q) + mtx_get(1, 1, q)*mtx_get(3, 1, q)));

	mtx_set(3, 2, dcm,
		2 * (mtx_get(3, 1, q)*mtx_get(4, 1, q) - mtx_get(1, 1, q)*mtx_get(2, 1, q)));

	mtx_set(3, 3, dcm,
		mtx_get(1, 1, q)*mtx_get(1, 1, q)
		- mtx_get(2, 1, q)*mtx_get(2, 1, q)
		- mtx_get(3, 1, q)*mtx_get(3, 1, q)
		+ mtx_get(4, 1, q)*mtx_get(4, 1, q));
}




void dcm_2_q(struct mtx_matrix* dcm, struct mtx_matrix* q) {

	float dcm_trace = 0.0;

	//Handle 90 Deg rotations
	dcm_trace = mtx_trace(dcm);

	if (dcm_trace>0) {

		mtx_set(1, 1, q, 0.5f*sqrtf(1.0f + dcm_trace));
		mtx_set(2, 1, q, (mtx_get(2, 3, dcm) - mtx_get(3, 2, dcm)) / (4.0f*mtx_get(1, 1, q)));
		mtx_set(3, 1, q, (mtx_get(3, 1, dcm) - mtx_get(1, 3, dcm)) / (4.0f*mtx_get(1, 1, q)));
		mtx_set(4, 1, q, (mtx_get(1, 2, dcm) - mtx_get(2, 1, dcm)) / (4.0f*mtx_get(1, 1, q)));

	}
	else if ((mtx_get(1, 1, dcm) > mtx_get(2, 2, dcm)) &&
		(mtx_get(1, 1, dcm) > mtx_get(3, 3, dcm))) {

		mtx_set(2, 1, q, 0.5f*sqrtf(1.0f + mtx_get(1, 1, dcm) - mtx_get(2, 2, dcm)
			- mtx_get(3, 3, dcm)));
		mtx_set(1, 1, q, (mtx_get(2, 3, dcm) - mtx_get(3, 2, dcm)) / (4.0f*mtx_get(2, 1, q)));
		mtx_set(3, 1, q, (mtx_get(1, 2, dcm) + mtx_get(2, 1, dcm)) / (4.0f*mtx_get(2, 1, q)));
		mtx_set(4, 1, q, (mtx_get(1, 3, dcm) + mtx_get(3, 1, dcm)) / (4.0f*mtx_get(2, 1, q)));

	}
	else if (mtx_get(2, 2, dcm) > mtx_get(3, 3, dcm)) {

		mtx_set(3, 1, q, -0.5f*sqrtf(1.0f + mtx_get(2, 2, dcm) - mtx_get(1, 1, dcm)
			- mtx_get(3, 3, dcm)));
		mtx_set(1, 1, q, (mtx_get(3, 1, dcm) - mtx_get(1, 3, dcm)) / (4.0f*mtx_get(3, 1, q)));
		mtx_set(2, 1, q, (mtx_get(1, 2, dcm) + mtx_get(2, 1, dcm)) / (4.0f*mtx_get(3, 1, q)));
		mtx_set(4, 1, q, (mtx_get(2, 3, dcm) + mtx_get(3, 2, dcm)) / (4.0f*mtx_get(3, 1, q)));

	}
	else {

		mtx_set(4, 1, q, 0.5f*sqrtf(1.0f + mtx_get(3, 3, dcm) - mtx_get(1, 1, dcm)
			- mtx_get(2, 2, dcm)));
		mtx_set(1, 1, q, (mtx_get(1, 2, dcm) - mtx_get(2, 1, dcm)) / (4.0f*mtx_get(4, 1, q)));
		mtx_set(2, 1, q, (mtx_get(1, 3, dcm) + mtx_get(3, 1, dcm)) / (4.0f*mtx_get(4, 1, q)));
		mtx_set(3, 1, q, (mtx_get(2, 3, dcm) + mtx_get(3, 2, dcm)) / (4.0f*mtx_get(4, 1, q)));

	}

	if (mtx_get(1, 1, q)<0) mtx_scale(q, -1.0f, q);
}

