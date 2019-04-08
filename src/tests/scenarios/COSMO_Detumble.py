''' '''
'''
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

'''


#
# Basilisk Scenario Script and Integrated Test
#
# Purpose:  Integrated test of the spacecraftPlus(), RWs, simpleNav() and
#           MRP_Feedback() modules.  Illustrates a 6-DOV spacecraft detumbling in orbit
#           while using the RWs to do the attitude control actuation.
# Author:   Hanspeter Schaub
# Creation Date:  Jan. 7, 2017
#


import pytest
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from Basilisk import __path__

# import general simulation support files
from Basilisk.utilities import SimulationBaseClass
from Basilisk.utilities import unitTestSupport  # general support file with common unit test functions
from Basilisk.utilities import simIncludeGravBody
from Basilisk.utilities import macros
from Basilisk.utilities import orbitalMotion
from Basilisk.utilities import simIncludeRW
from Basilisk.utilities import fswSetupRW
from Basilisk.utilities import RigidBodyKinematics

# import simulation related support
from Basilisk.simulation import spacecraftPlus
from Basilisk.simulation import simMessages
from Basilisk.simulation import sim_model
from Basilisk.simulation import simple_nav
from Basilisk.simulation import mag_meter
from Basilisk.simulation import imu_sensor
from Basilisk.simulation import coarse_sun_sensor
from Basilisk.simulation import reactionWheelStateEffector
from Basilisk.simulation import rwVoltageInterface
from Basilisk.simulation import torqueRodDynamicEffector
from Basilisk.simulation import extForceTorque
from Basilisk.simulation import eclipse
from Basilisk.simulation import dragDynamicEffector
from Basilisk.simulation import radiation_pressure


# import FSW Algorithm related support
from Basilisk.fswAlgorithms import inertial3D
from Basilisk.fswAlgorithms import inertial3DSpin
from Basilisk.fswAlgorithms import attTrackingError
from Basilisk.fswAlgorithms import MRP_Feedback
from Basilisk.fswAlgorithms import rwMotorVoltage
from Basilisk.fswAlgorithms import rwMotorTorque
from Basilisk.fswAlgorithms import maxwellLS
from Basilisk.fswAlgorithms import B_DOT
from Basilisk.fswAlgorithms import mag_attTrack
from Basilisk.fswAlgorithms import cssWlsEst
from Basilisk.fswAlgorithms import sunSafePoint


# import message declarations
from Basilisk.fswAlgorithms import fswMessages
bskPath = __path__[0]
from Basilisk import pyswice


def run(show_plots):
    '''Call this routine directly to run the tutorial scenario.'''

    # Create simulation variable names
    simTaskName = "simTask"
    simProcessName = "simProcess"

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()
    scSim.TotalSim.terminateSimulation()

    # set the simulation time variable used later on
    simulationTime = macros.min2nano(90.)

    #
    #  create the simulation process
    #
    dynProcess = scSim.CreateNewProcess(simProcessName)

    # create the dynamics task and specify the integration update time
    simulationTimeStep = macros.sec2nano(.1)
    dynProcess.addTask(scSim.CreateNewTask(simTaskName, simulationTimeStep))

    # if this scenario is to interface with the BSK Viz, uncomment the following lines
    # unitTestSupport.enableVisualization(scSim, dynProcess, simProcessName, 'earth')
    # The Viz only support 'earth', 'mars', or 'sun'

    #
    #   setup the simulation tasks/objects
    #

    # initialize spacecraftPlus object and set properties
    scObject = spacecraftPlus.SpacecraftPlus()
    scObject.ModelTag = "spacecraftBody"
    # define the simulation inertia
    I = [0.008, 0., 0.,
         0., 0.04, 0.,
         0., 0., 0.04]
    scObject.hub.mHub = 4.8  # kg - spacecraft mass
    scObject.hub.r_BcB_B = [[0.0], [0.0], [0.0]]  # m - position vector of body-fixed point B relative to CM
    scObject.hub.IHubPntBc_B = unitTestSupport.np2EigenMatrix3d(I)

    # add spacecraftPlus object to the simulation process
    scSim.AddModelToTask(simTaskName, scObject)

    # clear prior gravitational body and SPICE setup definitions
    gravFactory = simIncludeGravBody.gravBodyFactory()
    gravBodies = gravFactory.createBodies(['earth', 'sun', 'moon'])

    # setup Earth Gravity Body
    earth = gravBodies['earth']
    earth.isCentralBody = True  # ensure this is the central gravitational body
    mu = earth.mu
    simIncludeGravBody.loadGravFromFile(bskPath + '/supportData/LocalGravData/GGM03S.txt'
                                        , earth.spherHarm
                                        , 100)

    # attach gravity model to spaceCraftPlus
    scObject.gravField.gravBodies = spacecraftPlus.GravBodyVector(gravFactory.gravBodies.values())

    # setup simulation start data/time
    timeInitString = "2020 March 1 00:28:30.0"
    spiceTimeStringFormat = '%Y %B %d %H:%M:%S.%f'
    timeInit = datetime.strptime(timeInitString, spiceTimeStringFormat)
    # setup SPICE module
    gravFactory.createSpiceInterface(bskPath + '/supportData/EphemerisData/', timeInitString)
    gravFactory.spiceObject.zeroBase = 'Earth'

    # add SPICE interface to task list
    scSim.AddModelToTask(simTaskName, gravFactory.spiceObject, None, -1)
    # attach gravity model to spaceCraftPlus
    scObject.gravField.gravBodies = spacecraftPlus.GravBodyVector(gravFactory.gravBodies.values())

    # setup Sun Position
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'de430.bsp')  # solar system bodies
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'naif0011.tls')  # leap second file
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'de-403-masses.tpc')  # solar system masses
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'pck00010.tpc')  # generic Planetary Constants Kernel
    sunPositionMsg = simMessages.SpicePlanetStateSimMsg()
    sunInitialState = 1000 * pyswice.spkRead('SUN', timeInitString, 'J2000', 'EARTH')
    rN_sun = sunInitialState[0:2]  # meters
    vN_sun = sunInitialState[3:5]  # m/s
    sunPositionMsg.PositionVector = rN_sun
    sunPositionMsg.VelocityVector = vN_sun

    # setup Eclipse
    eclipseConfig = eclipse.Eclipse()
    eclipseConfig.ModelTag = "Eclipse"
    eclipseConfig.sunInMsgName = 'sun_planet_data'
    eclipseConfig.addPlanetName('earth')
    eclipseConfig.addPositionMsgName(scObject.scStateOutMsgName)
    scSim.AddModelToTask(simTaskName, eclipseConfig, None, 204)


    #
    #   set initial Spacecraft States
    #
    # setup the orbit using classical orbit elements
    oe = orbitalMotion.ClassicElements()
    orbitRadius = 415.28
    oe.a = (6371.0 + orbitRadius) * 1000.0  # meters
    oe.e = 0.0003449
    oe.i = 51.6388 * macros.D2R
    oe.Omega = 0.0 * macros.D2R
    oe.omega = 0.0 * macros.D2R
    oe.f =     80.0 * macros.D2R
    rN, vN = orbitalMotion.elem2rv(mu, oe)
    scObject.hub.r_CN_NInit = unitTestSupport.np2EigenVectorXd(rN)  # m   - r_CN_N
    scObject.hub.v_CN_NInit = unitTestSupport.np2EigenVectorXd(vN)  # m/s - v_CN_N
    scObject.hub.sigma_BNInit = [[0.1], [0.2], [-0.3]]  # sigma_BN_B
    scObject.hub.omega_BN_BInit = [[1.0 * macros.D2R], [-1.0 * macros.D2R], [1.0 * macros.D2R]]  # rad/s - omega_CN_B


    # setup extForceTorque module
    # the control torque is read in through the messaging system
    extFTObject = extForceTorque.ExtForceTorque()
    extFTObject.ModelTag = "externalDisturbance"
    # use the input flag to determine which external torque should be applied
    # Note that all variables are initialized to zero.  Thus, not setting this
    # vector would leave it's components all zero for the simulation.
    scObject.addDynamicEffector(extFTObject)
    scSim.AddModelToTask(simTaskName, extFTObject)


    # add the simple Navigation sensor module.  This sets the SC attitude, rate, position
    # velocity navigation message
    sNavObject = simple_nav.SimpleNav()
    sNavObject.ModelTag = "SimpleNavigation"
    sNavObject.outputAttName = "outAtt"
    scSim.AddModelToTask(simTaskName, sNavObject)

    #
    #   setup sensors
    #

    # Add Mag Meter
    MagMeter = mag_meter.MagMeter()
    MagMeter.ModelTag = "MagMeter"
    MagMeterNoise = 0.00000
    MagMeterBias = 0.0
    MagMeter.PMatrix = np.eye(3) * MagMeterNoise
    MagMeter.inclination = oe.i
    MagMeter.orbitRadius = oe.a / 1000  # 6371.0 + orbitRadius
    scSim.AddModelToTask(simTaskName, MagMeter)

    # set up inertial3D guidance module
    #attGuidanceConfig = inertial3D.inertial3DConfig()
    #attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
    #attGuidanceWrap.ModelTag = "inertial3D"
    #scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)
    #attGuidanceConfig.sigma_R0N = [0.0, 0.0, 0.0]
    #attGuidanceConfig.outputDataName = "guidanceInertial3D"

    # set up the inertial3D spin guidance module
    attGuidanceConfig = inertial3DSpin.inertial3DSpinConfig()
    attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
    attGuidanceWrap.ModelTag = "inertial3DSpin"
    scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)
    attGuidanceConfig.sigma_RN = [0.0, 0.0, 0.0]
    attGuidanceConfig.omega_spin = [0.0, 0.0, 0.0]
    attGuidanceConfig.outputDataName = "guidanceInertial3DSpin"
    attGuidanceConfig.inputRefName = "inertialSpinRef"

    # setup the attitude tracking error evaluation module
    attErrorConfig = attTrackingError.attTrackingErrorConfig()
    attErrorWrap = scSim.setModelDataWrap(attErrorConfig)
    attErrorWrap.ModelTag = "attErrorInertial3D"
    scSim.AddModelToTask(simTaskName, attErrorWrap, attErrorConfig)
    attErrorConfig.outputDataName = "attErrorInertial3DMsg"
    attErrorConfig.inputRefName = attGuidanceConfig.outputDataName
    attErrorConfig.inputNavName = sNavObject.outputAttName

    # setup the mag_attTrack Feedback control module
    mag_attTrackControlConfig = mag_attTrack.mag_attTrackConfig()
    mag_attTrackControlWrap = scSim.setModelDataWrap(mag_attTrackControlConfig)
    mag_attTrackControlWrap.ModelTag = "mag_attTrack"
    scSim.AddModelToTask(simTaskName, mag_attTrackControlWrap, mag_attTrackControlConfig)
    mag_attTrackControlConfig.inputMagMeterName = MagMeter.outputStateMessage
    mag_attTrackControlConfig.vehConfigInMsgName = "vehicleConfigName"
    mag_attTrackControlConfig.outputDataName = "LrRequested"
    mag_attTrackControlConfig.inputNavAttName = sNavObject.outputAttName
    mag_attTrackControlConfig.inputGuidName = attErrorConfig.outputDataName
    mag_attTrackControlConfig.K_sigma = 50000000
    mag_attTrackControlConfig.K_omega = 50000000
    mag_attTrackControlConfig.controlLaw = 3
    mag_attTrackControlConfig.use_rw_wheels = 0

    # setup the BDOT Feedback control module
    #bdotControlConfig = B_DOT.B_DOTConfig()
    #bdotControlWrap = scSim.setModelDataWrap(bdotControlConfig)
    #bdotControlWrap.ModelTag = "B_DOT"
    #scSim.AddModelToTask(simTaskName, bdotControlWrap, bdotControlConfig)
    #bdotControlConfig.inputMagMeterName = MagMeter.outputStateMessage
    #bdotControlConfig.vehConfigInMsgName = "vehicleConfigName"
    #bdotControlConfig.outputDataName = "LrRequested"
    #bdotControlConfig.K_detumble = 5000000.0

    torqueRodConfig = torqueRodDynamicEffector.torqueRodDynamicEffector()
    # torqueRodWrap = scSim.setModelDataWrap(torqueRodConfig)
    # scSim.AddModelToTask(simTaskName, torqueRodWrap, torqueRodConfig)
    torqueRodConfig.ModelTag = "torqueRods"
    torqueRodConfig.magFieldMsgName = MagMeter.outputStateMessage
    torqueRodConfig.cmdTorqueRodsMsgName = mag_attTrackControlConfig.outputDataName
    torqueRodConfig.torqueRodOutputMsgName = "torqueRodOutput"
    torqueRodConfig.MaxDipoleMoment = 0.11  # [Am^2]
    scObject.addDynamicEffector(torqueRodConfig)
    scSim.AddModelToTask(simTaskName, torqueRodConfig)

    # add drag dynamic effector (assumes simple cannonball model, attitude dependency not currently supported)
    #dragModelConfig = dragDynamicEffector.DragDynamicEffector()
    #dragModelConfig.modelType = "cannonball"
    #dragModelConfig.ModelTag = "cannonballDrag"
    #dragModelConfig.coreParams.velocityMag = 0.
    #dragModelConfig.coreParams.projectedArea = 0.068  # drag area in m^2
    #dragModelConfig.coreParams.dragCoeff = 2.0  # coefficient of drag
    #dragModelConfig.coreParams.comOffset = [0., 0.05, 0.05]  # distance from center of mass to  center of projected area
    #scObject.addDynamicEffector(dragModelConfig)
    #scSim.AddModelToTask(simTaskName, dragModelConfig)

    # add srp dynamic effector
    #srpModelConfig = radiation_pressure.RadiationPressure()
    #srpModelConfig.ModelTag = "srp"




    #
    #   Setup data logging before the simulation is initialized
    #
    numDataPoints = 100000
    samplingTime = simulationTime / (numDataPoints - 1)
    scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)
    scSim.TotalSim.logThisMessage(MagMeter.outputStateMessage, samplingTime)
    scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
    scSim.TotalSim.logThisMessage(torqueRodConfig.torqueRodOutputMsgName, samplingTime)
    scSim.TotalSim.logThisMessage(mag_attTrackControlConfig.outputDataName, samplingTime)
    #
    # create simulation messages
    #

    # create the FSW vehicle configuration message
    vehicleConfigOut = fswMessages.VehicleConfigFswMsg()
    vehicleConfigOut.ISCPntB_B = I  # use the same inertia in the FSW algorithm as in the simulation
    unitTestSupport.setMessage(scSim.TotalSim,
                                simProcessName,
                                mag_attTrackControlConfig.vehConfigInMsgName,
                                vehicleConfigOut)

    #
    #   initialize Simulation
    #
    scSim.InitializeSimulationAndDiscover()

    #
    #   configure a simulation stop time time and execute the simulation run
    #
    scSim.ConfigureStopTime(simulationTime)
    scSim.ExecuteSimulation()

    #
    #   retrieve the logged data
    #
    dataOmegaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".omega_BN_B", range(3))
    dataMagMeter = scSim.pullMessageLogData(MagMeter.outputStateMessage + ".mag_bf", range(3))
    dataSigmaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".sigma_BR", range(3))
    dataOmegaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".omega_BR_B", range(3))
    dataDipole = scSim.pullMessageLogData(torqueRodConfig.torqueRodOutputMsgName + ".dipole_constrained", range(3))
    dataTorque = scSim.pullMessageLogData(torqueRodConfig.torqueRodOutputMsgName + ".torque_constrained", range(3))

    plt.figure(1)
    for idx in range(1, 4):
        plt.plot(dataOmegaBN[:, 0] * macros.NANO2MIN, dataOmegaBN[:, idx]*macros.R2D,
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\omega_' + str(idx) + '$')
    plt.xlabel('Time [min]', fontsize=34)
    plt.ylabel('Angular Rates (deg/s) ', fontsize=12)
    plt.title('Spacecraft Angular Rates', fontsize=12)
    plt.tick_params(labelsize=12)
    p1ds = plt.axhline(y=1, color='r', linestyle='--')
    n1ds = plt.axhline(y=-1, color='r', linestyle='--')
    plt.legend((p1ds, n1ds), ('+1 deg/s', '-1 deg/s'), loc='upper right', fontsize=12)

    plt.figure(2)
    plt.plot(dataMagMeter[:, 0] * macros.NANO2HOUR, dataMagMeter[:, 1],
             color=unitTestSupport.getLineColor(1, 3),
             label='x')
    plt.plot(dataMagMeter[:, 0] * macros.NANO2HOUR, dataMagMeter[:, 2],
             color=unitTestSupport.getLineColor(2, 3),
             label='x')
    plt.plot(dataMagMeter[:, 0] * macros.NANO2HOUR, dataMagMeter[:, 3],
             color=unitTestSupport.getLineColor(3, 3),
             label='x')

    plt.xlabel('Time [hour]', fontsize=12)
    plt.ylabel('Tesla [T] ', fontsize=12)
    plt.title('Magnetometer Output', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.legend(loc='upper right', fontsize=12)

    # constrained dipole moment
    plt.figure(3)
    for idx in range(1, 4):
        plt.plot(dataDipole[:, 0] * macros.NANO2MIN, dataDipole[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label = '$m_' + str(idx) + '$')
    plt.xlabel('Time [min]', fontsize=34)
    plt.ylabel('Dipole Moment (A-m$^2$) ', fontsize=12)
    plt.title('Torque Rods Constrained Dipole Moment', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.legend(loc='upper right', fontsize=12)

    # constrained torque
    plt.figure(4)
    for idx in range(1, 4):
        plt.plot(dataTorque[:, 0] * macros.NANO2MIN, dataTorque[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\tau_' + str(idx) + '$')
    plt.xlabel('Time [min]', fontsize=34)
    plt.ylabel('Torque (N-m) ', fontsize=12)
    plt.title('Torque Rods Constrained Torque', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.legend(loc='upper right', fontsize=12)

    # attitude error
    plt.figure(5)
    for idx in range(1, 4):
        plt.plot(dataSigmaBR[:, 0] * macros.NANO2MIN, dataSigmaBR[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\tau_' + str(idx) + '$')
    plt.xlabel('Time [min]', fontsize=34)
    plt.ylabel('$\sigma$', fontsize=12)
    plt.title('MRP Components Relative to Reference', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.legend(loc='upper right', fontsize=12)



    if show_plots:
        plt.show()

    # close the plots being saved off to avoid over-writing old and new figures
    plt.close("all")

    return numDataPoints


#
# This statement below ensures that the unit test scrip can be run as a
# stand-along python script
#
if __name__ == "__main__":
    run(
        True,  # show_plots
    )
