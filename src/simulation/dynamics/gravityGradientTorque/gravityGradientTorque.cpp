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
#include "dynamics/gravityGradientTorque/gravityGradientTorque.h"
#include "architecture/messaging/system_messaging.h"
#include <iostream>
#include "utilities/avsEigenSupport.h"
#include "utilities/linearAlgebra.h"
#include "utilities/astroConstants.h"



/*! This is the constructor.  It sets some default initializers that can be
 overriden by the user.*/
gravityGradientTorque::gravityGradientTorque()
{
    /* setup default input message names.  These can be over-riden by the user */
    
    this->stateInMsgName = "scState";
    this->stateInMsgId = -1;
    
    return;
}

/*! The destructor.  Nothing of note is performed here*/
gravityGradientTorque::~gravityGradientTorque()
{
    return;
}

/*! No Action is performed in this function.
 @return void
 */
void gravityGradientTorque::SelfInit()
{
    return;
}

/*! This method is used to connect the input message.
 It sets the message ID based on what it finds for the input string.  If the
 message is not successfully linked, it will warn the user.
 @return void
 */
void gravityGradientTorque::CrossInit()
{
    //! Begin method steps
    //! - Find the message ID associated with the InputCmds string.

    
    this->stateInMsgId = SystemMessaging::GetInstance()->subscribeToMessage(this->stateInMsgName, sizeof(SCPlusStatesSimMsg), moduleID);
    if (stateInMsgId < 0) {
        BSK_PRINT(MSG_WARNING, "Did not find a valid sc plus message with name: %s", this->stateInMsgName.c_str());
    }
    
    this->vehicleConfigFswMsgID = SystemMessaging::GetInstance()->subscribeToMessage(this->vehicleConfigFswMsgName, sizeof(VehicleConfigFswMsg), moduleID);
    if (vehicleConfigFswMsgID < 0) {
        BSK_PRINT(MSG_WARNING, "Did not find a valid vehicle config message with name: %s", this->vehicleConfigFswMsgName.c_str());
    }
    
    return;

}

void gravityGradientTorque::linkInStates(DynParamManager& statesIn)
{
    return;
}


/*! This module writes output messages for output dipole and torque.
 @param CurrentClock The current time used for time-stamping the message
 @return void
 */
void gravityGradientTorque::writeOutputMessages(uint64_t currentClock)
{
    return;
}

/*! This method is used to read the incoming message and set the
 associated buffer structure.
 @return void
 */
void gravityGradientTorque::readInputMessages()
{
    SingleMessageHeader LocalHeader;
    memset(&LocalHeader, 0x0, sizeof(LocalHeader));
    memset(&this->stateInBuffer, 0x0, sizeof(SCPlusStatesSimMsg));
    
    if (this->stateInMsgId >= 0) {
        memset(&this->stateInBuffer, 0x0, sizeof(SCPlusStatesSimMsg));
        SystemMessaging::GetInstance()->ReadMessage(this->stateInMsgId, &LocalHeader,
                                                    sizeof(SCPlusStatesSimMsg),
                                                    reinterpret_cast<uint8_t*> (&this->stateInBuffer), moduleID);
    }
    
    
    if (this->vehicleConfigFswMsgID >= 0) {
        memset(sc.ISCPntB_B, 0x0, sizeof(VehicleConfigFswMsg));
        SystemMessaging::GetInstance()->ReadMessage(this->vehicleConfigFswMsgID, &LocalHeader,
                                                    sizeof(VehicleConfigFswMsg),
                                                    reinterpret_cast<uint8_t*> (&sc), moduleID);
    }
}

/*! This method is used to compute the RHS forces and torques.
    Note:   the module can set any of these three vecors, or a subset.  Regarding the external force, the
            matrix representations in the body (B) and inerial (N) frame components are treated as 2
            separate vectors.  Only set both if you mean to, as both vectors will be included.
 */
void gravityGradientTorque::computeForceTorque(double integTime)
{
	Eigen::Vector3d cmdVec;
    Eigen::Matrix3d dcm_BN;
    Eigen::MRPd     sigma_BN_eigen;
    Eigen::Vector3d r_BN_B;
    Eigen::Vector3d r_BN_N;    //! Begin method steps
    
    sigma_BN_eigen = cArray2EigenVector3d(this->stateInBuffer.sigma_BN);
    r_BN_N = cArray2EigenVector3d(this->stateInBuffer.r_BN_N);
    dcm_BN = sigma_BN_eigen.toRotationMatrix().transpose();
    r_BN_B = dcm_BN * r_BN_N;
    double r_BN_B_dbl[3];
    eigenVector3d2CArray(r_BN_B, r_BN_B_dbl);
    
    // print out r_BN_B_dbl
    for (int i = 0; i < 3; i++) {
        //BSK_PRINT(MSG_ERROR, "%f", this->navTrans.r_BN_N[i]);
    }
    
    double cmdVecOutput[3];
    double left_term[3];
    double right_term[3];
    double r_BN_B_norm;
    double fifth = 5.0;
    double I[3][3];
    
    //Assign I (debugged and verified)
    int i;
    int j;
    int ind = 0;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            I[i][j] = sc.ISCPntB_B[ind];
            ind++;
        }
    }

    r_BN_B_norm = v3Norm(r_BN_B_dbl);
    
    v3Scale(3*MU_EARTH / pow(r_BN_B_norm, fifth), r_BN_B_dbl, left_term);
    
    m33MultV3(I, r_BN_B_dbl, right_term);
    
    v3Cross(left_term, right_term, cmdVecOutput);
    
    BSK_PRINT(MSG_ERROR, "r norm: %f", r_BN_B_norm);
    cmdVec = cArray2EigenVector3d(cmdVecOutput);
    this->torqueExternalPntB_B = cmdVec;
    
    return;
}

void gravityGradientTorque::UpdateState(uint64_t CurrentSimNanos)
{
    this->readInputMessages();
    
    return;
}
