/* file: conversions.c
 * author: Jacob Cook
 * created on: 6/13/2014
 */

#define _USE_MATH_DEFINES

#include <math.h>
#include "conversions.h"
// TODO 999 What do we need here?
//#define CIRC_ORBIT (1e-3)

/* -- quat2euler123 -------------------------------------------------------
 *	Roll, pitch, yaw
 * ---------------------------------------------------------------------*/
void quat2euler321(float *q, float *e){

    e[0] = atan2f(2*(q[1]*q[2]+q[0]*q[3]),q[0]*q[0]+q[1]*q[1]-q[2]*q[2]-q[3]*q[3]);
    e[1] = asinf(-2*(q[1]*q[3]-q[0]*q[2]));
    e[2]= atan2f(2*(q[2]*q[3]+q[0]*q[1]),q[0]*q[0]-q[1]*q[1]-q[2]*q[2]+q[3]*q[3]);
}

///* -- orbit_period -------------------------------------------------------
// *
// * ---------------------------------------------------------------------*/
//float orbit_period(float a)
//{
//	return (2*M_PI*sqrt(pow(a,3)/MU_EARTH));
//}
//
///* -- rv2coe -------------------------------------------------------------
// * This function computes the classical orbital elements from the
// * ECI frame position and velocity vector.
// * ---------------------------------------------------------------------*/
//void rv2coe(float *x_orb, struct coe *oe)
//{
//	int32_t i;
//	float r_norm, v_norm, v_r, h_norm, N_norm, e_norm;
//	float xi;//, c1, c2;
//	float *r = x_orb, *v = r + 3;
//	float h[3], N[3], e[3];
//	float e_hat[3], r_hat[3], N_hat[3];
//	float z[] = {0.0, 0.0, 1.0};
//
//	/* compute position and velocity magnitudes */
//	r_norm = norm(r);
//	v_norm = norm(v);
//	v_r = dot(r,v)/r_norm;
//
//	/* angular momentum */
//	crossp(r,v,h);
//	h_norm = norm(h);
//
//	/* semi-major axis */
//	xi = pow(v_norm,2)/2 - MU_EARTH/r_norm;
//	oe->a = -MU_EARTH/(2*xi);
//
//	/* inclination */
//	oe->inc = acos(h[2]/h_norm);
//
//	/* node line */
//	crossp(z,h,N);
//	N_norm = norm(N);
//
//	/* right ascension or the ascending node */
//	oe->raan = acos(N[0]/N_norm);
//	if(N[2] < 0)
//		oe->raan = 2*M_PI - oe->raan;
//
//	/* eccentricity */
//	for(i=0;i<3;i++)
//	{
//		e[i] = 1/MU_EARTH*((pow(v_norm,2)-MU_EARTH/r_norm)*r[i]
//												- r_norm*v_r*v[i]);
//	}
//	e_norm = norm(e);
//	oe->e = e_norm;
//
//	/* unit vectors */
//	for(i=0;i<3;i++)
//	{
//		e_hat[i] = e[i]/e_norm;
//		r_hat[i] = r[i]/r_norm;
//		N_hat[i] = N[i]/N_norm;
//	}
//
//	if(e_norm < CIRC_ORBIT)
//	{
//		/* place argument of perigee at the line of nodes */
//		oe->omega = 0.0;
//		/* substitute the argument of latitude in for true anomaly */
//		oe->nu = acos(dot(N_hat, r_hat));
//		if(r[2] < 0)
//			oe->nu = 2*M_PI - oe->nu;
//	}
//	else
//	{
//		/* argument of perigee */
//		oe->omega = acos(dot(N_hat,e_hat));
//		if(e[2] < 0)
//			oe->omega = 2*M_PI - oe->omega;
//
//		/* true anomoly */
//		oe->nu = acos(dot(e_hat, r_hat));
//		if(v_r < 0)
//			oe->nu = 2*M_PI - oe->nu;
//	}
//}
//
///* -- coe2rv -------------------------------------------------------------
// * This function converts classical orbital elements into position and
// * velocity vectors expressed in the earth centered inertial frame.
// * ---------------------------------------------------------------------*/
//void coe2rv(struct coe *oe, float *x_orb)
//{
//	#define ROT(i,j) rot[ (i + j*3) ] /* col wise */
//
//	int32_t i, j;
//	float p;
//	float *r = x_orb, *v = r+3;
//	float Rpqw[3], Vpqw[3], rot[9];
//
//	/* compute semi parameter */
//	if(oe->e < CIRC_ORBIT)
//		p = oe->a;
//	else
//		p = oe->a*(1-pow(oe->e,2));
//
//	/* compute perifocal position */
//	Rpqw[0] = p*cos(oe->nu)/(1+oe->e*cos(oe->nu));
//	Rpqw[1] = p*sin(oe->nu)/(1+oe->e*cos(oe->nu));
//	Rpqw[2] = 0;
//
//	/* compute perifocal velocity */
//	Vpqw[0] = -sqrt(MU_EARTH/p)*sin(oe->nu);
//	Vpqw[1] = sqrt(MU_EARTH/p)*(oe->e+cos(oe->nu));
//	Vpqw[2] = 0;
//
//	/* get rotation matrix from perifocal to ECI frame */
//	rot313(oe->raan,oe->omega,oe->inc,rot);
//
//	/* rotate position and velocity from perifocal to ECI */
//	for(i=0;i<3;i++)
//	{
//		r[i] = 0.0;
//		v[i] = 0.0;
//		for(j=0;j<3;j++)
//		{
//			r[i] += ROT(i,j)*Rpqw[j];
//			v[i] += ROT(i,j)*Vpqw[j];
//		}
//	}
//}
//
///* -- rot313 -------------------------------------------------------------
// * This function builds a 313 rotation matrix. NOTE: Matrix stored column
// * wise.
// * ---------------------------------------------------------------------*/
//void rot313(float raan, float omega, float inc, float *R_313)
//{
//	float cR = cos(raan);
//	float sR = sin(raan);
//	float com = cos(omega);
//	float som = sin(omega);
//	float ci = cos(inc);
//	float si = sin(inc);
//
//	/* col 1 */
//	R_313[0] = cR*com - sR*som*ci;
//	R_313[1] = sR*com + cR*som*ci;
//	R_313[2] = som*si;
//	/* col 2 */
//	R_313[3] = -cR*som - sR*com*ci;
//	R_313[4] = -sR*som + cR*com*ci;
//	R_313[5] = com*si;
//	/* col 3 */
//	R_313[6] = sR*si;
//	R_313[7] = -cR*si;
//	R_313[8] = ci;
//}
//
///* -- rot3 -------------------------------------------------------------
// * This function builds a rotion matrix about the z axis. NOTE: matrix
// * stored column wise.
// * --------------------------------------------------------------------*/
//void rot3(float th, float *R_z)
//{
//	/* col 1 */
//	R_z[0] = cos(th);
//	R_z[1] = -sin(th);
//	R_z[2] = 0.0;
//	/* col 2 */
//	R_z[3] = sin(th);
//	R_z[4] = cos(th);
//	R_z[5] = 0.0;
//	/* col 3 */
//	R_z[6] = 0.0;
//	R_z[7] = 0.0;
//	R_z[8] = 1.0;
//}

/* -- norm ---------------------------------------------------------------
 *
 * ---------------------------------------------------------------------*/
float norm(float *v)
{
	return sqrtf( v[0]*v[0] + v[1]*v[1] + v[2]*v[2] );
}

/* -- norm quaternion ----------------------------------------------------
 *
 * ---------------------------------------------------------------------*/
float normq(float *v)
{
	return sqrtf( v[0]*v[0] + v[1]*v[1] + v[2]*v[2] + v[3]*v[3]);
}

/* -- crossp -------------------------------------------------------------
 *
 * --------------------------------------------------------------------*/

void crossp(float *u, float *v, float *x)
{
	x[0] = u[1]*v[2] - u[2]*v[1];
	x[1] = u[2]*v[0] - u[0]*v[2];
	x[2] = u[0]*v[1] - u[1]*v[0];
}

/* -- dot ----------------------------------------------------------------
*
* ---------------------------------------------------------------------*/
float dot(float *x, float *y)
{
	return ( x[0]*y[0] + x[1]*y[1] + x[2]*y[2] );
}

/* -- julian_date --------------------------------------------------------
 * this function returns the Julian date based on the the current time.
 * This function is dependant on J0 definition in the magSat_Config.h
 * file.
 * ---------------------------------------------------------------------*/
float julian_date(float t)
{
	return (float)J0 + t/86400.0f;
}

/* -- universal_time -----------------------------------------------------
 * This function calculates the Universal time from the Julian Date.
 * ---------------------------------------------------------------------*/
float universal_time(float JD)
{
	return (JD - 2451545.0f)/36525.0f;
}
//
//
///* -- JD2Cal -------------------------------------------------------------
// * Convert a Julian Date to a calendar date.
// *----------------------------------------------------------------------*/
//void JD2Cal( double JDate, double* cal )
//{
//  int64_t B,C,D,E;
//  double A, day_frac;
//
//  day_frac = modf( JDate+.5, &A );
//  cal[3] = (double)((int16_t)(day_frac*24));
//  cal[4] = (double)((int16_t)(day_frac*1440-((int16_t)cal[3])*60));
//  cal[5] = day_frac*86400.0 - cal[3]*3600.0 - cal[4]*60.0;
//
//  B = (int64_t)A + 1537;
//  C = (int64_t)((B-122.1)/365.25);
//  D = (int64_t)(365.25*C);
//  E = (int64_t)((B-D)/30.6001);
//  cal[2] = (double)(B-D-(int16_t)(30.6001*E));
//  cal[1] = (double)(E-1-12*(int16_t)(E/14));
//  cal[0] = (double)(C-4715-(int16_t)((7+cal[1])/10));
//
//}
//
///* -- JD2DoY -------------------------------------------------------------
// * Convert a time in Julian Days to a year and day of year representation.
// * ---------------------------------------------------------------------*/
//void JD2DOY( double JDate, int32_t* yr_doy )
//{
//  uint8_t have_leap = 0;
//
//  int32_t month_start[12] = {0,31,59,90,120,151,181,212,243,273,304,334};
//  int32_t month_start_leap[12] = {0,31,60,91,121,152,182,213,244,274,305,335};
//
//  double cal[6];
//
//  /*
//   *  Calculate the calendar date from the julian date.
//   */
//  JD2Cal( JDate, cal );
//
//  /*
//   *  Determine if we are in a leap year.
//   */
//  have_leap = ((((int32_t)cal[0]%4==0)&&((int32_t)cal[0]%100!=0))||((int32_t)cal[0]%400==0))?1:0;
//
//  /*
//   *  Store the year in the output array
//   */
//  yr_doy[0] = (int32_t) cal[0];
//
//  /*
//   *  Calculate the day of year based on if it is a leap year or not.  Store
//   *  the value in the output array.
//   */
//  if( have_leap ){
//    yr_doy[1] = month_start_leap[(int32_t)cal[1]-1] + (int32_t)cal[2];
//  }else{
//    yr_doy[1] = month_start[(int32_t)cal[1]-1] + (int32_t)cal[2];
//  }
//
//}
/* -- gmst --------------------------------------------------------------
 *
 * function prototype:
 * 	th_gmst = gmst(t)
 *		t = time in seconds past Epoch (J0)
 * --------------------------------------------------------------------*/
#define GMST_C0 (67310.54841)
#define GMST_C1 (876600.0*3600.0 + 8640184.812866)
#define GMST_C2 (0.093104)
#define GMST_C3 (6.2e-6)
#define GMST_SEC2RAD (7.2722e-5) /* M_PI/240.0/180.0 */

double gmst(double t)
{
	double JD, T_UT1, th_gmst, gmst_sec;

	/* compute current Julian Date */
	JD = julian_date((float)t);
	T_UT1 = universal_time((float)JD);

	/*PRINT("JD = %f\n\r", JD);*/
	/*PRINT("T_UT1 = %f\n\r",T_UT1);*/

	/* compute greenwich mean standard time (Vallado eq. 3-47) */
	gmst_sec = GMST_C0 + GMST_C1*T_UT1 +
						GMST_C2*pow(T_UT1,2) + GMST_C3*pow(T_UT1, 3);

	/*PRINT("gmst_sec = %f\n\r", gmst_sec);*/

	/* reduce down to within one revolution */
	gmst_sec = fmod(gmst_sec, 86400);
	/*PRINT("gmst_sec = %f\n\r", gmst_sec);*/

	/* convert to radians */
	th_gmst = GMST_SEC2RAD*gmst_sec;

	if(th_gmst < 0)
		th_gmst += 2*M_PI;

	/*PRINT("th_gmst = %f\n\r", th_gmst);*/
	return th_gmst;
}
//
///* -- eci_2_orbit -------------------------------------------------------
// * rotates a vector in the ECI frame to the orbital frame.  This function
// * assumes a circular orbit.
// * --------------------------------------------------------------------*/
//
//void eci_2_orbit(float *eci, float *r, float *v, float *orbit)
//{
//	#define R(i,j) _R[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	/* Earth centered inertial to orbital reference frame */
//	float v_norm, r_norm, y_norm;
//	static	float _R[9], y[3];
//	int32_t i,j;
//
//	v_norm = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);
//	r_norm = sqrt(r[0]*r[0]+r[1]*r[1]+r[2]*r[2]);
//
//	crossp(v,r,y);
//	y_norm = sqrt(y[0]*y[0]+y[1]*y[1]+y[2]*y[2]);
//
//	for(i=1;i<=3;i++)
//	{
//		R(1,i) = v[i-1]/v_norm;
//		R(2,i) = y[i-1]/y_norm;
//		R(3,i) = -r[i-1]/r_norm;
//	}
//
//	for(i=1;i<=3;i++)
//	{
//		orbit[i-1] = 0.0;
//		for(j=1;j<=3;j++)
//		{
//			orbit[i-1] += R(i,j)*eci[j-1];
//		}
//	}
//	#undef R
//}
//
///* -- ecef_2_eci --------------------------------------------------------
// * Rotates a vector given in the ECEF frame to the ECI frame based on the
// * current Greenwich Mean Standard Time.
// * --------------------------------------------------------------------*/
//
//void ecef_2_eci(float *ecef, float th_gmst, float *eci)
//{
//	#define Rz_th(i,j) _Rz_th[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	float _Rz_th[9];
//	int32_t i,j;
//
//	rot3(-th_gmst, _Rz_th);
//
//	for(i=1;i<=3;i++)
//	{
//		eci[i-1] = 0.0;
//		for(j=1;j<=3;j++)
//			eci[i-1] += Rz_th(i,j)*ecef[j-1];
//	}
//
//	#undef Rz_th
//}
//
///* -- eci_2_ecef --------------------------------------------------------
// * Rotates an ECI vector to ECEF frame based on the current Greenwich
// * Mean Standard Time.
// * --------------------------------------------------------------------*/
//
//void eci_2_ecef(float *eci, float th_gmst, float *ecef)
//{
//	#define Rz_th(i,j) _Rz_th[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//
//	float _Rz_th[9];
//	int32_t i,j;
//
//	rot3(th_gmst, _Rz_th);
//
//	for(i=1;i<=3;i++)
//	{
//		ecef[i-1] = 0.0;
//		for(j=1;j<=3;j++)
//			ecef[i-1] += Rz_th(i,j)*eci[j-1];
//	}
//
//	#undef Rz_th
//}
//
///* -- llr_2_ecef --------------------------------------------------------
// * computes the ECEF position vector from the Lat Long and radius.
// *
// * llr[0] = Lat [rad]
// * llr[1] = Lon [rad]
// * llr[2] = radius [km]
// * --------------------------------------------------------------------*/
//
//void llr_2_ecef(float *llr, float *ecef)
//{
//	ecef[0] = llr[2]*cos(llr[0])*cos(llr[1]);
//	ecef[1] = llr[2]*cos(llr[0])*sin(llr[1]);
//	ecef[2] = llr[2]*sin(llr[0]);
//}
//
///* -- ecef_2_llr --------------------------------------------------------
// * Computes the Latitude, Longitude and Radius of the ECEF position
// * vector.
// *
// * llr[0] = Lat [rad]
// * llr[1] = Lon [rad]
// * llr[2] = radius [km]
// * --------------------------------------------------------------------*/
//
//void ecef_2_llr(float *ecef, float *llr)
//{
//	/* radius [r] */
//	llr[2] = sqrt(ecef[0]*ecef[0] + ecef[1]*ecef[1] + ecef[2]*ecef[2]);
//	/* longitude [phi] */
//	llr[1] = atan2(ecef[1],ecef[0]);
//	/* lattitude [th] */
//	llr[0] = asin(ecef[2]/llr[2]);
//}
//
///* -- hat --
// * build a skew symmetric from a vector belonging to R^3.
// *
// * function prototype:
// * 		hat(x, x_h);
// *     	x 	= [ x1  x2  x3]
// * 			x_h = [ 0  -x3  x2]
// *				 		[ x3  0  -x1]
// *				 		[-x2  x1  0 ]
// */
//
//void hat(float *x_, float *x_h_)
//{
//	/* Allow Matlab like calling */
//	#define x_h(i,j)	x_h_[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define x(i) 			x_[ (i)-1 ]
//	int32_t i;
//
//	/* zeros down the diag */
//	for(i=1;i<=3;i++)
//		x_h(i,i) = 0.0;
//
//	/* upper tri */
//	x_h(1,2) = -x(3);
//	x_h(1,3) = x(2);
//	x_h(2,3) = -x(1);
//
//	/* lower tri */
//	x_h(2,1) = x(3);
//	x_h(3,1) = -x(2);
//	x_h(3,2) = x(1);
//
//	#undef x_h
//	#undef x
//}
//
//
///* -- hat_4x4 --
// *
// * function prototype:
// * 		hat(x, x_h);
// *     	x 	= [ x1  x2  x3]
// *
// * 			x_h = [ 0   x3 -x2  x1]
// *				 		[-x3  0   x1  x2]
// *				 		[ x2 -x1  0   x3]
// *						[-x1 -x2 -x3   0]
// */
//
//void hat_4x4(float *x_, float *x_h_)
//{
//	/* Allow Matlab like calling */
//	#define x_h(i,j)	x_h_[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define x(i) 			x_[ (i)-1 ]
//	int32_t i;
//
//	/* zeros down the diag */
//	for(i=1;i<=3;i++)
//		x_h(i,i) = 0.0;
//
//	/* upper tri */
//	x_h(1,2) = x(3);
//	x_h(1,3) = -x(2);
//	x_h(1,4) = x(1);
//	x_h(2,3) = x(1);
//	x_h(2,4) = x(2);
//	x_h(3,4) = x(3);
//
//	/* lower tri */
//	x_h(2,1) = -x(3);
//	x_h(3,1) = x(2);
//	x_h(4,1) = -x(1);
//	x_h(3,2) = -x(1);
//	x_h(4,2) = -x(2);
//	x_h(4,3) = -x(3);
//
//	#undef x_h
//	#undef x
//}
//
//
//
///* -- exp_n --
// * this function computes the matrix exponetial (rotation matrix)
// * of  -xi_hat. If the principal angle is zero it returns the Identity
// * matrix.
// *
// * function prototype:
// *  	exp_n(xi, R);
// * 			xi = th [ e1 e2 e3]
// * 			R  = f(xi)
// *				 = R(-xi)
// *       	 = e^(-xi_hat)
// *       	 = I - e_h sin(th) + e_h^2 2*sin(th/2)
// */
//
//void exp_n(float *xi_, float *exp_nxi_)
//{
//	#define xi_h(i,j) 			_xi_h[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define exp_nxi(i,j) 	exp_nxi_[ ((i) -1) + ((j)-1)*3 ] /* col wise */
//  #define I(i,j) 				( (i == j) ? 1 : 0 ) /* Identity matrix */
//
//	float _th, _xi_h2, _sin_th2, _sin2_th2, _sin_th;
//	float _xi_h[9];
//	int32_t i,j,k;
//
//	/* get th and e_h from xi */
//	_th = sqrt(xi_[0]*xi_[0] + xi_[1]*xi_[1] + xi_[2]*xi_[2]);
//
//  if(_th == 0)
//	{
//		/* the rotation is equal to the identity matrix */
//		/* we do this to avoid a divide by zero situation */
//		for(i=1;i<=3;i++)
//			for(j=1;j<=3;j++)
//				exp_nxi(i,j) = I(i,j);
//	}
//	else
//	{
//		/* compute hat operator */
//		hat(xi_, _xi_h);
//
//		_sin_th2 = sin(_th/2);
//		_sin2_th2 = _sin_th2*_sin_th2/_th/_th;
//		_sin_th = sin(_th)/_th;
//
//		/* compute Rotation matrix */
//		for(i=1;i<=3;i++)
//		{
//			for(j=1;j<=3;j++)
//			{
//				_xi_h2 = 0.0;
//				for(k=1;k<=3;k++)
//				{
//					_xi_h2 += xi_h(i,k)*xi_h(k,j);
//				}
//				exp_nxi(i,j) = I(i,j) - _sin_th*xi_h(i,j) + 2*_sin2_th2*_xi_h2;
//			}
//		}
//	}
//
//	#undef e_h
//	#undef exp_nxi
//	#undef I
//}
//
///* -- idexp_n --
// * this function computes the inverse of the operator dexp_(-xi)
// *
// * function prototype:
// *	idexp_n(xi, idexp_nxi);
// * 		xi 		= th [ e1 e2 e3 ]
// * 		idexp_nxi	= f(xi)
//						= [dexp(-xi)]^-1
// * 			 		= I + 1/2 xi_h - (th cot(th/2) - 2)/(2 th^2) xi_h^2
// */
//
//void idexp_n(float *xi_, float *idexp_nxi_)
//{
//	#define xi_h(i,j)				_xi_h[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define xi_h2(i,j)			_xi_h2[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define idexp_nxi(i,j) 	idexp_nxi_[ ((i)-1) + ((j)-1)*3 ] /* col wise */
//	#define I(i,j) 					( (i == j) ? 1 : 0 ) 	/* identity matrix */
//
//	float _th, _cot_th2, _th_cot_th2_2;
//	float _xi_h[9], _xi_h2[9];
//	int32_t i,j,k;
//
//	/* get th and e_h from xi */
//	_th = sqrt(xi_[0]*xi_[0] + xi_[1]*xi_[1] + xi_[2]*xi_[2]);
//
//	if(_th == 0)
//	{
//		/* if the rotation is equal to the identity matrix */
//		/* we do this to avoid a divide by zero situation */
//		for(i=1;i<=3;i++)
//			for(j=1;j<=3;j++)
//				idexp_nxi(i,j) = I(i,j);
//	}
//	else
//	{
//		/* hat xi */
//		hat(xi_, _xi_h);
//
//		_cot_th2 = 1.0/tan(_th/2.0);
//		/*PRINT("%f \n\r",_cot_th2);*/
//		_th_cot_th2_2 = .5*(_th*_cot_th2-2.0)/(_th*_th);
//		/*PRINT("%f \n\r",_th_cot_th2_2);*/
//
//		/* xi_h^2 */
//		for(i=1;i<=3;i++)
//		{
//			for(j=1;j<=3;j++)
//			{
//				xi_h2(i,j) = 0.0;
//				for(k=1;k<=3;k++)
//				{
//					xi_h2(i,j) += xi_h(i,k)*xi_h(k,j);
//				}
//				/*PRINT("%f ", xi_h2(i,j));*/
//			}
//			/*PRINT("\n\r");*/
//		}
//
//		/* compute idexp_nxi */
//		for(i=1;i<=3;i++)
//		{
//			for(j=1;j<=3;j++)
//			{
//				idexp_nxi(i,j) = I(i,j) + .5*xi_h(i,j) - _th_cot_th2_2 * xi_h2(i,j);
//			}
//		}
//	}
//
//	#undef xi_h
//	#undef idexp_nxi
//	#undef I
//}
//
///* -- orb_2_xi -----------------------------------------------------------
// *
// * ---------------------------------------------------------------------*/
//void orb_2_xi(float *orb, float *xi_orb)
//{
//	uint32_t i;
//	float x[] = {0, 0, -1};
//	float e[3];
//	float th, norm_e, norm_orb;
//
//	/* rotation axis */
//	crossp(x, orb, e);
//	norm_e = norm(e);
//
//
//	/* rotation angle */
//	norm_orb = norm(orb);
//	th = acos(dot(x,orb)/norm_orb);
//
//	/* compute principal rotation vector */
//	for(i=0;i<3;i++)
//	{
//		xi_orb[i] = th*e[i]/norm_e;
//	}
//
//}
//
///* -- xi_ab --------------------------------------------------------------
// *
// * ---------------------------------------------------------------------*/
//void xi_ab(float *xi_a, float *xi_b, float *xi_ab)
//{
//	uint32_t i;
//	float th_a, th_b, th_ab;
//	float sth_a, cth_a, sth_b, cth_b, sth_ab;
//	float e_a[3], e_b[3], a_X_b[3], e_ab[3];
//
//	/* compute thetas */
//	th_a = norm(xi_a);
//	th_b = norm(xi_b);
//
//	if(th_a != 0)
//	{
//		for(i=0;i<3;i++)
//		{
//			e_a[i] = xi_a[i]/th_a;
//		}
//	}
//	else
//	{
//		for(i=0;i<3;i++)
//		{
//			e_a[i] = 0.0;
//		}
//	}
//
//	if(th_b != 0)
//	{
//		for(i=0;i<3;i++)
//		{
//			e_b[i] = xi_b[i]/th_b;
//		}
//	}
//	else
//	{
//		for(i=0;i<3;i++)
//		{
//			e_b[i] = 0.0;
//		}
//	}
//
//	/* calculate th_ab */
//	sth_a = sin(th_a/2);
//	cth_a = cos(th_a/2);
//	sth_b = sin(th_b/2);
//	cth_b = cos(th_b/2);
//
//	th_ab = 2*acos(cth_a*cth_b - sth_a*sth_b*dot(e_a,e_b));
//
//	/* calculate e_ab */
//	crossp(e_a, e_b, a_X_b);
//	sth_ab = sin(th_ab/2);
//	if(th_ab != 0)
//	{
//		for(i=0;i<3;i++)
//		{
//			e_ab[i] = (cth_b*sth_a*e_a[i] + cth_a*sth_b*e_b[i] +
//								sth_a*sth_b*a_X_b[i])/sth_ab;
//			xi_ab[i] = th_ab*e_ab[i];
//		}
//	}
//	else
//	{
//		for(i=0;i<3;i++)
//		{
//			xi_ab[i] = 0.0;
//		}
//	}
//}
//
///* -- xi_ab --------------------------------------------------------------
// *
// * ---------------------------------------------------------------------*/

// # ERH 10

