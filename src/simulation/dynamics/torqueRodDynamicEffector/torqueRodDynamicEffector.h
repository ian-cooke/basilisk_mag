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

#ifndef TORQUE_ROD_DYNAMIC_EFFECTOR_H
#define TORQUE_ROD_DYNAMIC_EFFECTOR_H

#include "_GeneralModuleFiles/sys_model.h"
#include "../_GeneralModuleFiles/dynamicEffector.h"
#include "../../simFswInterfaceMessages/cmdTorqueRodsIntMsg.h"
#include "../../simFswInterfaceMessages/MagMeterIntMsg.h"
#include "../../simFswInterfaceMessages/torqueRodOutputIntMsg.h"
#include "../../../utilities/bsk_Print.h"


class torqueRodDynamicEffector: public SysModel, public DynamicEffector{
public:
    torqueRodDynamicEffector();
    ~torqueRodDynamicEffector();

    void SelfInit();
    void CrossInit();
    void UpdateState(uint64_t CurrentSimNanos);
    void linkInStates(DynParamManager& statesIn);
    void writeOutputMessages(uint64_t currentClock);
    void readInputMessages();
    void computeForceTorque(double integTime);

private:
    int64_t cmdTorqueRodsMsgID;           //!< -- Message ID for incoming data
    int64_t magFieldMsgID;
    int64_t torqueRodOutputMsgID;
    CmdTorqueRodsIntMsg DipoleMomentCmd;
    MagMeterIntMsg MagFieldCurrent;
    torqueRodOutputIntMsg torqueRodOutput;


public:
    Eigen::Vector3d torqueRods_B;
    Eigen::Vector3d current_mag_bf;
    Eigen::Vector3d dipole_mom;
    Eigen::Vector3d extTorquePntB_B;    //!< [Nm] external torque in body frame components
    std::string cmdTorqueRodsMsgName;     //!< -- message used to read torque command inputs
    std::string magFieldMsgName;
    std::string torqueRodOutputMsgName;
    double MaxDipoleMoment;

};


#endif
