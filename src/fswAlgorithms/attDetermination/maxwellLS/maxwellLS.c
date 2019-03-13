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

#include "attDetermination/maxwellLS/maxwellLS.h"
#include "simulation/utilities/linearAlgebra.h"
#include "simFswInterfaceMessages/macroDefinitions.h"
#include "simulation/utilities/mtx.h"
#include "simulation/utilities/rigidBodyKinematics.h"
#include "simulation/utilities/astroConstants.h"
#include <string.h>
#include <math.h>

/*! This method initializes the ConfigData for theCSS WLS estimator.
 It checks to ensure that the inputs are sane and then creates the
 output message
 @return void
 @param ConfigData The configuration data associated with the CSS WLS estimator
 */
void SelfInit_maxwellLS(maxwellLSConfig *ConfigData, uint64_t moduleID)
{
    
    /*! Begin method steps */
    /*! - Create output message for module */
    ConfigData->navStateOutMsgId = CreateNewMessage(ConfigData->navStateOutMsgName, sizeof(NavAttIntMsg), "NavAttIntMsg", moduleID);
	ConfigData->sunpointOutMsgID = CreateNewMessage(ConfigData->sunpointOutMsgName, sizeof(sunpointIntMsg), "sunpointIntMsg", moduleID);

}

/*! This method performs the second stage of initialization for the CSS sensor
 interface.  It's primary function is to link the input messages that were
 created elsewhere.
 @return void
 @param ConfigData The configuration data associated with the CSS interface
 */
void CrossInit_maxwellLS(maxwellLSConfig *ConfigData, uint64_t moduleID)
{
    /*! - Loop over the number of sensors and find IDs for each one */
    ConfigData->cssDataInMsgID = subscribeToMessage(ConfigData->cssDataInMsgName,
                                                    sizeof(CSSArraySensorIntMsg), moduleID);
}

/*! This method performs a complete reset of the module.  Local module variables that retain
 time varying states between function calls are reset to their default values.
 @return void
 @param ConfigData The configuration data associated with the guidance module
 */
void Reset_maxwellLS(maxwellLSConfig *ConfigData, uint64_t callTime, uint64_t moduleID)
{
    uint64_t ClockTime;
    uint32_t ReadSize;

	ConfigData->sunDirection.timeTag = 0.0;
    ConfigData->sunlineOutBuffer.timeTag = 0.0;
    v3SetZero(ConfigData->sunlineOutBuffer.sigma_BN);
    v3SetZero(ConfigData->sunlineOutBuffer.omega_BN_B);
//    v4SetZero(ConfigData->q_des_RN.q_des_RN);

    
    return;
}

/*! This method computes a least squares fit with the given parameters.  It
 treats the inputs as though they were double dimensioned arrays but they
 are all singly dimensioned for ease of use
 @return success indicator (1 for good, 0 for fail)
 @param numActiveCss The count on input measurements
 @param H The predicted pointing vector for each measurement
 @param W the weighting matrix for the set of measurements
 @param y the observation vector for the valid sensors
 @param x The output least squares fit for the observations
 */


 void Update_maxwellLS(maxwellLSConfig *ConfigData, uint64_t callTime,
                      uint64_t moduleID)
{

    uint64_t ClockTime;
    uint32_t ReadSize;
    CSSArraySensorIntMsg InputBuffer;
    uint32_t i;


    /*! Begin method steps*/
    /*! - Read the input parsed CSS sensor data message*/
    memset(&InputBuffer, 0x0, sizeof(CSSArraySensorIntMsg));
    ReadMessage(ConfigData->cssDataInMsgID, &ClockTime, &ReadSize,
                sizeof(CSSArraySensorIntMsg),
                (void*) (&InputBuffer), moduleID);


    float sun_sens_map[] = {
        0.0,0.707107,0.707107,
        0.707107,0.0,0.707107,
        0.0,-0.707107,0.707107,
        -0.707107,0.0,0.707107,
        0.0,-0.965926,-0.258819,
        -0.707107,-0.353553,-0.612372,
        0.0,0.258819,-0.965926,
        0.707107,-0.353553,-0.612372};

//    float sun_sens_map[] = {
//        0.866,0.000,-0.500,     //+X1
//        0.866,-0.433,0.250,     //+X2
//        0.866,0.433,0.250,      //+X3
//        0.500,0.866,0.000,      //+Y3
//        0.500,-0.866,0.000,     //-Y2
//        0.000,-0.866,-0.500,    //-Y1
//        0.500,0.866,0.000,      //+Y2
//        0.000,0.866,-0.500,     //+Y1
//        0.000,0.866,0.500,      //+Y4
//        0.500,-0.866,0.000,     //-Y3
//        0.000,-0.866,0.500,     //-Y4
//        0.866,-0.433,-0.250,   //-X3
//        0.866,0.000,0.500,     //-X1
//        0.866,0.433,-0.250};   //-X2


    int SS_COUNT = (sizeof(sun_sens_map)/sizeof(sun_sens_map[0]))/3;
    float sun_sens_values[(sizeof(sun_sens_map)/sizeof(sun_sens_map[0]))/3];
    float ss_v_cutoff = 0.7;
    int num_active_css = 0;
    int k = 0;
    int n = 0;
    int j = 0;
    float sun_sens_map_act[8*3];
    float y[8];
    float sHatBdyCmd[3] = {-1.0,0.0,0.0};


    /*! - Get least squares fit for sun pointing vector*/
	float sun_vec[3];
	float qBR[4];


    /* Check sensor voltage against threshold*/
    for (i=0;i<SS_COUNT;i++)
    {
        sun_sens_values[i] = InputBuffer.CosValue[i];
        if (sun_sens_values[i]>ss_v_cutoff)
        {
            sun_sens_values[i]=InputBuffer.CosValue[i];
            sun_sens_map_act[k] = sun_sens_map[n];
            sun_sens_map_act[k+1] = sun_sens_map[n+1];
            sun_sens_map_act[k+2] = sun_sens_map[n+2];
            y[j] = sun_sens_values[i];
            k=k+3;
            j=j+1;
            num_active_css++;

        } else {
            sun_sens_values[i] = 0.0;
        }
        n = n+3;
    }
//    printf("sun: %d\n", num_active_css);

    if (num_active_css == 0) {
        sun_vec[0] = 0.0;
        sun_vec[1] = 0.0;
        sun_vec[2] = 0.0;
    } else {
        compute_LS(num_active_css, &sun_sens_map_act, &sun_sens_values, sun_vec);
    }

    create_qBR(sun_vec,qBR,sHatBdyCmd);
    for (i=0;i<3;i++)
    {
        ConfigData->sunlineOutBuffer.vehSunPntBdy[i] = sun_vec[i];
    }

    for (i=0;i<4;i++) {
        ConfigData->sunDirection.q_BR[i] = qBR[i];
    }
//    printf("%f %f %f %f\n", ConfigData->sunDirection.q_BR[0],
//     ConfigData->sunDirection.q_BR[1],
//     ConfigData->sunDirection.q_BR[2],
//     ConfigData->sunDirection.q_BR[3]);


    WriteMessage(ConfigData->navStateOutMsgId, callTime, sizeof(NavAttIntMsg),
                 &(ConfigData->sunlineOutBuffer), moduleID);

    WriteMessage(ConfigData->sunpointOutMsgID, callTime, sizeof(sunpointIntMsg),
                 &(ConfigData->sunDirection), moduleID);
    return;
}

void compute_LS(int num_active_css, float *H, float *y, float x[3])
{
    struct mtx_matrix H_mtx;
    struct mtx_matrix HT_mtx;
    struct mtx_matrix y_meas;
    struct mtx_matrix xhat;
    struct mtx_matrix tmp_mtxa;
    struct mtx_matrix tmp_mtxb;
    struct mtx_matrix tmp_va;

    int32_t i;
    if (num_active_css == 1) {
        mtx_create(1,3,H,&H_mtx);
        mtx_scale(&H_mtx,y[0],&H_mtx);
        for (i=0;i<3;i++){
            x[i] = mtx_get(1,i+1,&H_mtx);
        }
    } else if (num_active_css == 2) {
        // Equation 3.10 O'Keefe
        // xhat = (H^T H)^-1 H^T y
        mtx_create_ones(2,2,&tmp_mtxa);
        mtx_create_ones(3,2,&tmp_mtxb);

        mtx_create(2,3,H,&H_mtx);
        mtx_create(2,1,y,&y_meas);
        mtx_create_ones(3,1,&xhat);
        mtx_create_ones(3,2,&HT_mtx);

        mtx_trans(&H_mtx,&HT_mtx);
        mtx_mult(&H_mtx,&HT_mtx,&tmp_mtxa);
        mtx_inv(&tmp_mtxa,&tmp_mtxa);
        mtx_mult(&HT_mtx,&tmp_mtxa,&tmp_mtxb);
        mtx_mult(&tmp_mtxb,&y_meas,&xhat);

        for (i=0;i<3;i++) {
            x[i] = mtx_get(i+1,1,&xhat);
        }
    } else if (num_active_css > 2) {
        // Equation 3.9 O'Keefe
        // xhat = H^T (H H^T)^-1 y
        mtx_create_ones(num_active_css,num_active_css,&tmp_mtxa);
        mtx_create_ones(num_active_css,3,&tmp_mtxb);

        mtx_create(num_active_css,3,H,&H_mtx);
        mtx_create(num_active_css,1,y,&y_meas);
        mtx_create_ones(3,1,&xhat);
        mtx_create_ones(3,num_active_css,&HT_mtx);

        mtx_mult(&HT_mtx,&H_mtx,&tmp_mtxa);
        mtx_inv(&tmp_mtxa,&tmp_mtxa);
        mtx_mult(&tmp_mtxa,&HT_mtx,&tmp_mtxb);
        mtx_mult(&tmp_mtxb,&y_meas,&xhat);

        for (i=0;i<3;i++) {
            x[i] = mtx_get(i+1,1,&xhat);
        }
    }
    /* Normalize sun vector */
    for (i=0;i<3;i++) {
        x[i] = x[i]/norm(x);
    }



}

void cal_sun_sens(struct mtx_matrix *sun_sens_volt, struct mtx_matrix *sun_sens_bfmtx,
                  struct mtx_matrix *sun_sens_cal_bfmtx, float ss_v_cutoff){


    int32_t i;
    int32_t SS_COUNT = 14;
    struct mtx_matrix cur_sens;
    struct mtx_matrix cur_sum;
    struct mtx_matrix tmp_143a;
    struct mtx_matrix tmp_141a;
    

    //    int sun_sens_pair[13] = {11,12,13,6,8,4,5,9,8,9,1,2,3}; //Flight Mapping
    int sun_sens_pair[14] = {13,14,12,10,7,9,5,11,6,4,8,3,1,2}; //Sim Mapping
    
    
    mtx_create_ones(1,3,&cur_sens);
    mtx_create_ones(SS_COUNT,3,&tmp_143a);
    mtx_create_ones(SS_COUNT,1,&tmp_141a);
    mtx_create_ones(SS_COUNT,3,&cur_sum);
    
    /*Compare sun sensor against sun sensor on opposite side of craft*/
    for (i=1;i<SS_COUNT+1;i++){
        /*If voltage is less than voltage at opposite location, set to 0*/
        if(mtx_get(i,1,sun_sens_volt)>mtx_get(sun_sens_pair[i-1],1,sun_sens_volt) &&
           mtx_get(i,1,sun_sens_volt)>ss_v_cutoff){
            mtx_set(i,1,sun_sens_cal_bfmtx, mtx_get(i,1,sun_sens_volt));
        } else {
            mtx_set(i,1,sun_sens_cal_bfmtx, 0);
        }
    }
}


void create_qBR(float *sun_vec, float *qBR, float *sHatBdyCmd){


    struct mtx_matrix sun_vec_bf;
    struct mtx_matrix panel_vec_bf;
    struct mtx_matrix tmp_33;
    struct mtx_matrix tmp_31a;
    struct mtx_matrix tmp_31b;
    struct mtx_matrix tmp_31c;
    struct mtx_matrix tmp_31;
    int32_t i;

    float panel_vec[3] = {-1.0,0.0,0.0};
    float vec_norm;
    float phi;
    float dot_prod = 0.0;
    float sun_vec_norm;
    float sun_vec_normalized;
    float ctSNormalized;
	float sNorm;
	float e_hat[3];
	float eHat180_B[3] = {0.0,0.0,-1.0};
	float minUnitMag = 0.1;
	float sunAngleErr;
	float smallAngle = 0.1;
	float v1[3] = {1.0,0.0,0.0};


/*********** CALCULATION FOR eHAT180_B **************/
//    mtx_create_ones(3,3,&tmp_33);
//	mtx_create_ones(3,1,&tmp_31a);
//	mtx_create(3,1,panel_vec,&tmp_31b);
//	mtx_create(3,1,v1,&tmp_31c);
//	mtx_ss(&tmp_31b,&tmp_33);
//	mtx_mult(&tmp_33,&tmp_31c,&tmp_31a);
//	for (i=0;i<3;i++) {
//	    eHat180_B[i] = mtx_get(i+1,1,&tmp_31a);
//	}
//	printf("MAX: %f %f %f\n", eHat180_B[0], eHat180_B[1], eHat180_B[2]);
//
//	for (i=0;i<3;i++) {
//	    eHat180_B[i] = eHat180_B[i]/norm(eHat180_B);
//	}

//    if (norm(eHat180_B) < 0.1) {
//        v1[0] = 0.0;
//        v1[1] = 1.0;
//        v1[2] = 0.0;
//        mtx_create(3,1,v1,&tmp_31c);
//        mtx_mult(&tmp_33,&tmp_31c,&tmp_31a);
//        for (i=0;i<3;i++) {
//	        eHat180_B[i] = mtx_get(i+1,1,&tmp_31a);
//	    }
//	}
/*********************************************/

    
    /************************* sunSafePoint ********************/
    /* Normlize Sun Vec*/
	sNorm = norm(sun_vec);
	for (i=0;i<3;i++) {
	    sun_vec[i] = sun_vec[i]/sNorm;
	}
	/* Compute heading error relative to sun direction vector */
	if (sNorm > minUnitMag) {
	    ctSNormalized = (sHatBdyCmd[0]*sun_vec[0] + sHatBdyCmd[1]*sun_vec[1] + sHatBdyCmd[2]*sun_vec[2])/sNorm;
	    ctSNormalized = fabs(ctSNormalized) > 1.0 ?
	    ctSNormalized/fabs(ctSNormalized) : ctSNormalized;
	    sunAngleErr = acos(ctSNormalized);


	    /* sun heading and body axis are essentially alligned, set attitude error to 0 */
	    if (sunAngleErr < smallAngle) {
	        qBR[0] = 1.0;
	        qBR[1] = 0.0;
	        qBR[2] = 0.0;
	        qBR[3] = 0.0;
	    } else {
	        if ((M_PI - sunAngleErr) < smallAngle) {
                /* the commanded body vector nearly is opposite the sun heading */
	            for (i=0;i<3;i++){
	                e_hat[i] = eHat180_B[i];
	            }
	        } else {
                /* normal case where sun and commanded body vectors are not aligned */
                mtx_create(3,1,sun_vec,&tmp_31a);
	            mtx_create(3,1,sHatBdyCmd,&tmp_31b);
	            mtx_create_ones(3,3,&tmp_33);
	            mtx_create_ones(3,1,&tmp_31c);
	            mtx_ss(&tmp_31a,&tmp_33);
	            mtx_mult(&tmp_33,&tmp_31b, &tmp_31c);
	            for (i=0;i<3;i++) {
	                e_hat[i] = mtx_get(i+1,1,&tmp_31c);
	            }

	        }
	        for (i=0;i<3;i++) {
	            e_hat[i] = e_hat[i]/norm(e_hat);
	        }
	        qBR[0] = cos(sunAngleErr/2);
	        qBR[1] = e_hat[0] * sin(sunAngleErr/2);
	        qBR[2] = e_hat[1] * sin(sunAngleErr/2);
	        qBR[3] = e_hat[2] * sin(sunAngleErr/2);
	    }
	} else {
	    qBR[0] = 1.0;
	    qBR[1] = 0.0;
	    qBR[2] = 0.0;
	    qBR[3] = 0.0;
	}
    
    return;

}




