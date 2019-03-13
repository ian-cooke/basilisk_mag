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
#include "sensors/mag_meter/mag_meter.h"
#include "architecture/messaging/system_messaging.h"
#include "utilities/rigidBodyKinematics.h"
#include "utilities/linearAlgebra.h"
#include "simFswInterfaceMessages/macroDefinitions.h"
#include <iostream>
#include <cstring>
#include <math.h>
#include "utilities/avsEigenSupport.h"
#include "utilities/gauss_markov.h"

MagMeter::MagMeter()
{
    this->mag_bf_out.fill(0.0);
    this->mag_hill_out.fill(0.0);
    this->PreviousTime = 0;
    this->CallCounts = 0;
    this->messagesLinked = false;
    this->inputStateID = -1;
    this->inputStateMessage = "inertial_state_output";
    this->outputStateMessage = "magnetic_field";
    this->OutputBufferCount = 2;
    this->sensorTimeTag = 0;
    this->errorModel = GaussMarkov(3);
    this->PMatrix.fill(0.0);
    this->AMatrix.fill(0.0);
    this->walkBounds.fill(0.0);
    this->senBias.fill(0.0);
    this->inclination = 0.0;
    return;
}

MagMeter::~MagMeter()
{
    return;
}

bool MagMeter::LinkMessages()
{
    this->inputStateID = SystemMessaging::GetInstance()->subscribeToMessage(
        this->inputStateMessage, sizeof(SCPlusStatesSimMsg), this->moduleID);


    return(inputStateID >= 0);
}

void MagMeter::SelfInit()
{
    //! Begin method steps
    uint64_t numStates = 3;
    this->outputStateID = SystemMessaging::GetInstance()->
        CreateNewMessage(this->outputStateMessage, sizeof(MagMeterIntMsg),
        OutputBufferCount, "MagMeterIntMsg", this->moduleID);

    this->AMatrix.setIdentity(numStates, numStates);

    //! - Alert the user if the noise matrix was not the right size.  That'd be bad.
    if(this->PMatrix.size() != numStates*numStates)
    {
        std::cerr << __FILE__ <<": Your process noise matrix (PMatrix) is not 3*3.";
        std::cerr << "  Quitting."<<std::endl;
        return;
    }
    if(this->walkBounds.size() != numStates){
        std::cerr << __FILE__ <<": Your walkbounds is not size 3.";
        std::cerr << "  Quitting."<<std::endl;
        return;
    }
    this->errorModel.setNoiseMatrix(this->PMatrix);
    this->errorModel.setRNGSeed(this->RNGSeed);
    this->errorModel.setUpperBounds(this->walkBounds);
}

void MagMeter::CrossInit()
{
    messagesLinked = this->LinkMessages();
}

void MagMeter::readInputMessages()
{
    SingleMessageHeader localHeader;

    if(!this->messagesLinked)
    {
        this->messagesLinked = LinkMessages();
    }

    memset(&this->scState, 0x0, sizeof(SCPlusStatesSimMsg));
    if(this->inputStateID >= 0)
    {
        SystemMessaging::GetInstance()->ReadMessage(this->inputStateID, &localHeader,
                                                    sizeof(SCPlusStatesSimMsg), reinterpret_cast<uint8_t*>(&scState), this->moduleID);
        this->sensorTimeTag = localHeader.WriteClockNanos;
    }

}



void MagMeter::computeMagField(uint64_t CurrentSimNanos)
{
    double w_e = 7.2921159E-5; // [rad/s]
    double gamma_m = 0.296705972839036; // [rad]
    double M = 7.838E6;
    double inc = this->inclination;
    double beta_m;
    double theta_dot;
    double theta;
    double t;
    double H_b[3];
    double dcm_BN[3][3];
    double dcm_HN[3][3];
    double dcm_HN_T[3][3];
    double dcm_BNHN[3][3];
    double B_b[3];
    double xi_m;
    double eta_m;
    double r;


    r = pow(pow(scState.r_BN_N[0],2) + pow(scState.r_BN_N[1],2) + pow(scState.r_BN_N[2],2),0.5)/1000;


    t = CurrentSimNanos*1.0E-9;
//    printf("%f\n",this->orbitRadius);
//    r = v3Norm(scState.r_BN_N);
    theta_dot = sqrt(398600.0/pow(r,3));
    theta = theta_dot*t;
    double EA[3] = {0.0,inc,theta};
    beta_m = w_e*t;

    xi_m = acos(cos(inc)*cos(gamma_m) + sin(inc)*sin(gamma_m)*cos(-beta_m));
    eta_m = asin(sin(gamma_m)*sin(-beta_m)/sin(xi_m));

    //H_b[0] = M/(pow(r,3))*cos(theta_dot*t - eta_m)*sin(xi_m);
    //H_b[1] = M/(pow(r,3))*cos(xi_m);
    //H_b[2] = -2*M/(pow(r,3))*sin(theta_dot*t - eta_m)*sin(xi_m);

    H_b[0] = -2*M/(pow(r,3))*sin(theta_dot*t - eta_m)*sin(xi_m);
    H_b[1] = M/(pow(r,3))*cos(theta_dot*t - eta_m)*sin(xi_m);
    H_b[2] = M/(pow(r,3))*cos(xi_m);

    MRP2C(scState.sigma_BN,dcm_BN);
    Euler3132C(EA,dcm_HN);
    m33Transpose(dcm_HN,dcm_HN_T);
    m33MultM33t(dcm_BN,dcm_HN_T,dcm_BNHN);
    m33MultV3(dcm_BNHN,H_b,B_b);





    this->mag_hill_out = cArray2EigenVector3d(H_b);
    this->mag_bf_out = cArray2EigenVector3d(B_b);
    this->sensedValues.timeTag = this->sensorTimeTag;


}


void MagMeter::computeSensorErrors()
{
    this->errorModel.setPropMatrix(this->AMatrix);
    this->errorModel.computeNextState();
    this->navErrors = this->errorModel.getCurrentState();
}

void MagMeter::applySensorErrors()
{
    Eigen::Vector3d MagErrors; // Mag noise plus bias
    MagErrors = this->navErrors + this->senBias;
    this->mag_bf_out += MagErrors;
}


void MagMeter::writeOutputMessages(uint64_t CurrentSimNanos)
{

    MagMeterIntMsg LocalOutput;
    eigenVector3d2CArray(this->mag_bf_out, LocalOutput.mag_bf);
    eigenVector3d2CArray(this->mag_hill_out, LocalOutput.mag_hill);

    SystemMessaging::GetInstance()->WriteMessage(this->outputStateID, CurrentSimNanos,
                                                 sizeof(MagMeterIntMsg), reinterpret_cast<uint8_t*> (&LocalOutput), this->moduleID);
}

void MagMeter::UpdateState(uint64_t CurrentSimNanos)
{
    this->readInputMessages();
    this->computeSensorErrors();
    this->computeMagField(CurrentSimNanos);
    this->applySensorErrors();
    this->writeOutputMessages(CurrentSimNanos);
    this->PreviousTime = CurrentSimNanos;
}
