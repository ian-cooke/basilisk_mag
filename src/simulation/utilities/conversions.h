/* file: conversions.h
 * author: Jacob Cook
 * created on: 6/13/2014
 */

#ifndef __CONVERSIONS_H
#define __CONVERSIONS_H

#include "types.h"

/* Orbit constants */
#define MU_EARTH 	(3.986004415e5) /* Gravitational Constant [km^3/s^2] */

/* Julian date of the start time of the orbit 
 * May 1, 2015 00:00:00 
 * Use matlab function JulianDate.m for J0 calculation
 *
 * NOTE: propagate JD as JD = J0 + ((sec/60+min)/60 + h)/2
 */
#define J0 (2.4571435e6) /* May 1, 2015 00:00:00 */

/* Classical Orbital Elements */
struct coe
{
	float a;
	float inc;
	float e;
	float raan;
	float omega;
	float nu;
};

/* function prototypes */
void quat2euler321(float *q, float *e);
float orbit_period(float a);
void rv2coe(float *x_orb, struct coe *oe);
void coe2rv(struct coe *oe, float *x_orb);
void rot313(float raan, float omega, float inc, float *R_313);
void rot_z(float th, float *R_z);
float norm(float *v);
float normq(float *v);
void crossp(float *u, float *v, float *x);
float dot(float *x, float *y);
float julian_date(float t);
float universal_time(float JD);
void JD2Cal( double JDate, double* cal );
void JD2DOY( double JDate, int32_t* yr_doy );
double gmst(double t);
void eci_2_orbit(float *eci, float *r, float *v, float *orbit);
void ecef_2_eci(float *ecef, float th_gmst, float *eci);
void eci_2_ecef(float *eci, float th_gmst, float *ecef);
void llr_2_ecef(float *llr, float *ecef);
void ecef_2_llr(float *ecef, float *llr);
void hat_4x4(float *x_, float *x_h_);
void hat(float *x_, float *x_h_);
void exp_n(float *xi_, float *exp_nxi_);
void idexp_n(float *xi_, float *idexp_nxi_);
void orb_2_xi(float *orb, float *xi_orb);
void xi_ab(float *xi_a, float *xi_b, float *xi_ab);

#endif
