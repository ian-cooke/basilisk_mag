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

#ifndef GRAVITY_GRADIENT_TORQUE_H
#define GRAVITY_GRADIENT_TORQUE_H

#include "_GeneralModuleFiles/sys_model.h"
#include "../_GeneralModuleFiles/dynamicEffector.h"
#include "../simulation/utilities/avsEigenMRP.h"
#include "../../simMessages/scPlusStatesSimMsg.h"
#include "../../../fswAlgorithms/fswMessages/vehicleConfigFswMsg.h"
#include "../../../utilities/bsk_Print.h"


class gravityGradientTorque: public SysModel, public DynamicEffector{
public:
    gravityGradientTorque();
    ~gravityGradientTorque();

    void SelfInit();
    void CrossInit();
    void UpdateState(uint64_t CurrentSimNanos);
    void linkInStates(DynParamManager& statesIn);
    void writeOutputMessages(uint64_t currentClock);
    void readInputMessages();
    void computeForceTorque(double integTime);

private:
    SCPlusStatesSimMsg scPlusStates;
    int64_t scPlusStatesSimMsgID;           //!< -- Message ID for incoming data
    VehicleConfigFswMsg sc;
    int64_t vehicleConfigFswMsgID;
public:
    std::string scPlusStatesSimMsgName;     //!< -- message used to read torque command inputs
    std::string vehicleConfigFswMsgName;
    Eigen::Vector3d extTorquePntB_B;    //!< [Nm] external torque in body frame components

};


#endif
