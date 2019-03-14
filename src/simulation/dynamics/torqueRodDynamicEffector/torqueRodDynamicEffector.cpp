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
#include "dynamics/torqueRodDynamicEffector/torqueRodDynamicEffector.h"
#include "architecture/messaging/system_messaging.h"
#include <iostream>
#include "utilities/avsEigenSupport.h"
#include "utilities/linearAlgebra.h"



/*! This is the constructor.  It sets some default initializers that can be
 overriden by the user.*/
torqueRodDynamicEffector::torqueRodDynamicEffector()
{
    /* initialize the 3 output vectors to zero */
    this->torqueRods_B.fill(0.0);
    this->current_mag_bf.fill(0.0);
    this->dipole_mom.fill(0.0);

    /* setup default input message names.  These can be over-riden by the user */
    cmdTorqueRodsMsgName = "torqueRods_B_cmds";
    cmdTorqueRodsMsgID = -1;
    
    magFieldMsgName = "current_mag_bf";
    magFieldMsgID = -1;
    
    torqueRodOutputMsgName = "torqueRods_output";
    torqueRodOutputMsgID = -1;
    return;
}

/*! The destructor.  Nothing of note is performed here*/
torqueRodDynamicEffector::~torqueRodDynamicEffector()
{
    return;
}

/*! No Action is performed in this function.
 @return void
 */
void torqueRodDynamicEffector::SelfInit()
{
    SystemMessaging *messageSys = SystemMessaging::GetInstance();
    this->torqueRodOutputMsgID =  messageSys->CreateNewMessage(this->torqueRodOutputMsgName, sizeof(torqueRodOutputIntMsg), 2, "torqueRodOutputIntMsg", this->moduleID);
    return;
}

/*! This method is used to connect the input message.
 It sets the message ID based on what it finds for the input string.  If the
 message is not successfully linked, it will warn the user.
 @return void
 */
void torqueRodDynamicEffector::CrossInit()
{
    //! Begin method steps
    //! - Find the message ID associated with the InputCmds string.
    cmdTorqueRodsMsgID = SystemMessaging::GetInstance()->subscribeToMessage(this->cmdTorqueRodsMsgName,sizeof(CmdTorqueRodsIntMsg), moduleID);
    
    magFieldMsgID = SystemMessaging::GetInstance()->subscribeToMessage(this->magFieldMsgName,sizeof(MagMeterIntMsg), moduleID);
    
    torqueRodOutputMsgID = SystemMessaging::GetInstance()->subscribeToMessage(this->torqueRodOutputMsgName,sizeof(torqueRodOutputMsgID), moduleID);
    
    /* zero the input message vectors */
    memset(&(this->DipoleMomentCmd.dipole_moment), 0x0, 3*sizeof(double));
    return;
}

void torqueRodDynamicEffector::linkInStates(DynParamManager& statesIn)
{

}


/*! This module writes output messages for output dipole and torque.
 @param CurrentClock The current time used for time-stamping the message
 @return void
 */
void torqueRodDynamicEffector::writeOutputMessages(uint64_t currentClock)
{
    SystemMessaging *messageSys = SystemMessaging::GetInstance();
    
    for (int i = 0; i < 3; i ++) {
        torqueRodOutput.dipole_constrained[i] = DipoleMomentCmd.dipole_moment[i];
        torqueRodOutput.torque_constrained[i] = torqueExternalPntB_B[i];
    }
    messageSys->WriteMessage(this->torqueRodOutputMsgID, currentClock,
                             sizeof(torqueRodOutputIntMsg), reinterpret_cast<uint8_t*> (&torqueRodOutput), this->moduleID);
     return;
     
}

/*! This method is used to read the incoming message and set the
 associated buffer structure.
 @return void
 */
void torqueRodDynamicEffector::readInputMessages()
{
    SingleMessageHeader LocalHeader;

    //! - If the input message ID is invalid, return without touching states
    if(this->cmdTorqueRodsMsgID >= 0)
    {
        memset(DipoleMomentCmd.dipole_moment, 0x0, sizeof(CmdTorqueRodsIntMsg));
        SystemMessaging::GetInstance()->ReadMessage(this->cmdTorqueRodsMsgID, &LocalHeader,
                                                    sizeof(CmdTorqueRodsIntMsg),
                                                    reinterpret_cast<uint8_t*> (&DipoleMomentCmd), moduleID);
    }
    
    if(magFieldMsgID >= 0)
    {
        memset(MagFieldCurrent.mag_bf, 0x0, sizeof(MagMeterIntMsg));
        SystemMessaging::GetInstance()->ReadMessage(magFieldMsgID, &LocalHeader,
                                                    sizeof(MagMeterIntMsg),
                                                    reinterpret_cast<uint8_t*> (&MagFieldCurrent),
                                                    moduleID);
    }
}

/*! This method is used to compute the RHS forces and torques.
    Note:   the module can set any of these three vecors, or a subset.  Regarding the external force, the
            matrix representations in the body (B) and inerial (N) frame components are treated as 2
            separate vectors.  Only set both if you mean to, as both vectors will be included.
 */
void torqueRodDynamicEffector::computeForceTorque(double integTime)
{
	Eigen::Vector3d cmdVec;
    //! Begin method steps
    
    double cmdVecOutput[3];
    int i;
    for (i=0;i<3;i++){
        //BSK_PRINT(MSG_ERROR, "Dipole Moment Before is: %f", DipoleMomentCmd.dipole_moment[i]);
        if(DipoleMomentCmd.dipole_moment[i] > MaxDipoleMoment)
            DipoleMomentCmd.dipole_moment[i] = MaxDipoleMoment;
        if(DipoleMomentCmd.dipole_moment[i] < -MaxDipoleMoment)
            DipoleMomentCmd.dipole_moment[i] = -MaxDipoleMoment;
        //BSK_PRINT(MSG_ERROR, "Dipole Moment after is: %f", DipoleMomentCmd.dipole_moment[i]);
    }
    
    v3Cross(DipoleMomentCmd.dipole_moment, MagFieldCurrent.mag_bf, cmdVecOutput);
    
    cmdVec = cArray2EigenVector3d(cmdVecOutput);
    this->torqueExternalPntB_B = cmdVec;
    
    return;
}

void torqueRodDynamicEffector::UpdateState(uint64_t CurrentSimNanos)
{
    this->readInputMessages();
    
    writeOutputMessages(CurrentSimNanos);
    
    return;
}
