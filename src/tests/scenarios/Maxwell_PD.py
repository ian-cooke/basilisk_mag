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


# import FSW Algorithm related support
from Basilisk.fswAlgorithms import inertial3DSpin
from Basilisk.fswAlgorithms import inertial3D
from Basilisk.fswAlgorithms import attTrackingError
from Basilisk.fswAlgorithms import rwMotorVoltage
from Basilisk.fswAlgorithms import rwMotorTorque
from Basilisk.fswAlgorithms import maxwellLS
from Basilisk.fswAlgorithms import QUAT_PD
from Basilisk.fswAlgorithms import cssWlsEst
from Basilisk.fswAlgorithms import sunSafePoint


# import message declarations
from Basilisk.fswAlgorithms import fswMessages
bskPath = __path__[0]
from Basilisk import pyswice


def run(show_plots, useUnmodeledTorque, useJitterSimple, useRWVoltageIO):
    '''Call this routine directly to run the tutorial scenario.'''

    # Create simulation variable names
    simTaskName = "simTask"
    simProcessName = "simProcess"

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()
    scSim.TotalSim.terminateSimulation()

    # set the simulation time variable used later on
    simulationTime = macros.sec2nano(500.)

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
    I = [0.0511, 0., 0.,
         0., 0.1522, 0.,
         0., 0., 0.1179]
    scObject.hub.mHub = 10.0  # kg - spacecraft mass
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

    #
    #   set initial Spacecraft States
    #
    # setup the orbit using classical orbit elements
    oe = orbitalMotion.ClassicElements()
    orbitRadius = 550.0
    oe.a = (6371.0 + orbitRadius) * 1000.0  # meters
    oe.e = 0.0001
    oe.i = 55.0 * macros.D2R
    oe.Omega = 0.0 * macros.D2R
    oe.omega = 0.0 * macros.D2R
    oe.f = 180.0 * macros.D2R
    rN, vN = orbitalMotion.elem2rv(mu, oe)
    scObject.hub.r_CN_NInit = unitTestSupport.np2EigenVectorXd(rN)  # m   - r_CN_N
    scObject.hub.v_CN_NInit = unitTestSupport.np2EigenVectorXd(vN)  # m/s - v_CN_N
    scObject.hub.sigma_BNInit = [[0.1], [0.2], [-0.3]]  # sigma_BN_B
    scObject.hub.omega_BN_BInit = [[0.05 * macros.D2R], [0.05 * macros.D2R], [0.05 * macros.D2R]]  # rad/s - omega_CN_B

    #
    # add RW devices
    #
    # Make a fresh RW factory instance, this is critical to run multiple times
    rwFactory = simIncludeRW.rwFactory()

    # store the RW dynamical model type
    varRWModel = rwFactory.BalancedWheels
    if useJitterSimple:
        varRWModel = rwFactory.JitterSimple

    # create each RW by specifying the RW type, the spin axis gsHat, plus optional arguments
    RW1 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0.906307787036650, 0], maxMomentum=0.02, Omega=0.#RPM
                           , RWModel=varRWModel,
                           )
    RW2 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0, 0.906307787036650], maxMomentum=0.02, Omega=0.#RPM
                           , RWModel=varRWModel,
                           )
    RW3 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, -0.906307787036650, 0], maxMomentum=0.02, Omega=0.#RPM
                           , RWModel=varRWModel,
                           )
    RW4 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0, -0.906307787036650], maxMomentum=0.02, Omega=0.#RPM
                           , RWModel=varRWModel,
                           )

    numRW = rwFactory.getNumOfDevices()

    # create RW object container and tie to spacecraft object
    rwStateEffector = reactionWheelStateEffector.ReactionWheelStateEffector()
    rwStateEffector.InputCmds = "reactionwheel_cmds"
    rwFactory.addToSpacecraft("ReactionWheels", rwStateEffector, scObject)

    # add RW object array to the simulation process
    scSim.AddModelToTask(simTaskName, rwStateEffector, None, 2)

    if useRWVoltageIO:
        rwVoltageIO = rwVoltageInterface.RWVoltageInterface()
        rwVoltageIO.ModelTag = "rwVoltageInterface"

        # set module parameters(s)
        rwVoltageIO.setGains(np.array([0.2 / 10.] * 3)) # [Nm/V] conversion gain

        # Add test module to runtime call list
        scSim.AddModelToTask(simTaskName, rwVoltageIO)

    # setup extForceTorque module
    # the control torque is read in through the messaging system
    extFTObject = extForceTorque.ExtForceTorque()
    extFTObject.ModelTag = "externalDisturbance"
    # use the input flag to determine which external torque should be applied
    # Note that all variables are initialized to zero.  Thus, not setting this
    # vector would leave it's components all zero for the simulation.
    if useUnmodeledTorque:
        extFTObject.extTorquePntB_B = [[0.00003], [-0.00003], [0.00003]]
    scObject.addDynamicEffector(extFTObject)
    scSim.AddModelToTask(simTaskName, extFTObject)

    # add the simple Navigation sensor module.  This sets the SC attitude, rate, position
    # velocity navigation message
    sNavObject = simple_nav.SimpleNav()
    sNavObject.ModelTag = "SimpleNavigation"
    scSim.AddModelToTask(simTaskName, sNavObject)

    #
    #   setup sensors
    #

    # Add IMU Sensor
    ImuSensor = imu_sensor.ImuSensor()
    ImuSensor.ModelTag = "imusensor"
    r_SB_B = np.array([0.0, 0.0, 0.0])  # Sensor position wrt body frame origin
    ImuSensor.sensorPos_B = np.array(r_SB_B)

    # IMU Parameters
    accelLSBIn = 0.0  # Not Used
    gyroLSBIn = 0.0001  # Discretization value (least significant bit)
    senRotBiasIn = 0.0  # Rotational sensor bias
    senRotMaxIn = 50.0  # Gyro saturation value
    gyroScale = [1., 1., 1.]  # Scale factor for each axis
    errorBoundsGryo = [0] * 3  # Bounds random walk
    gyroNoise = 0.0  # Noise

    ImuSensor.setLSBs(accelLSBIn, gyroLSBIn)
    ImuSensor.senRotBias = np.array([senRotBiasIn] * 3)
    ImuSensor.senRotMax = senRotMaxIn
    ImuSensor.gyroScale = np.array(gyroScale)
    ImuSensor.PMatrixGyro = np.eye(3) * gyroNoise
    ImuSensor.walkBoundsGyro = np.array(errorBoundsGryo)
    ImuSensor.OutputDataMsg = "AngVelocities"

    # add IMU to Simulation Process
    scSim.AddModelToTask(simTaskName, ImuSensor)

    # Add Mag Meter
    MagMeter = mag_meter.MagMeter()
    MagMeter.ModelTag = "MagMeter"
    MagMeterNoise = 0.0
    MagMeterBias = 0.0
    ImuSensor.senRotBias = np.array([MagMeterBias] * 3)
    MagMeter.PMatrix = np.eye(3) * MagMeterNoise
    MagMeter.inclination = oe.i
    MagMeter.orbitRadius = oe.a / 1000  # 6371.0 + orbitRadius
    scSim.AddModelToTask(simTaskName, MagMeter)

    # # Add Coarse Sun Sensors
    cssConstellation = coarse_sun_sensor.CSSConstellation()
    CSSOrientationList = [
        [0.866, 0.000, -0.500],  # 1 - 13 G
        [0.866, -0.433, 0.250],  # 2 - 14 G
        [0.866, 0.433, 0.250],  # 3 - 12 G
        [0.500, 0.866, 0.000],  # 4 - 10 G
        [0.500, -0.866, 0.000],  # 5 - 7 G
        [0.000, -0.866, -0.500],  # 6 - 9 G
        [0.500, 0.866, 0.000],  # 7 - 5 G
        [0.000, 0.866, -0.500],  # 8 - 11 G
        [0.000, 0.866, 0.500],  # 9 - 6 G
        [0.500, -0.866, 0.000],  # 10 - 4 G
        [0.000, -0.866, 0.500],  # 11 - 8 G
        [0.866, -0.433, -0.250],  # 12 - 3 G
        [0.866, 0.000, 0.500],  # 13 - 1 G
        [0.866, 0.433, -0.250]  # 14 - 2 G
    ]

    # CSSOrientationList = [
    #     [0.70710678118654746, -0.5, 0.5],
    #     [0.70710678118654746, -0.5, -0.5],
    #     [0.70710678118654746, 0.5, -0.5],
    #     [0.70710678118654746, 0.5, 0.5],
    #     [-0.70710678118654746, 0, 0.70710678118654757],
    #     [-0.70710678118654746, 0.70710678118654757, 0.0],
    #     [-0.70710678118654746, 0, -0.70710678118654757],
    #     [-0.70710678118654746, -0.70710678118654757, 0.0]
    # ]

    for CSSHat in CSSOrientationList:
        newCSS = coarse_sun_sensor.CoarseSunSensor()
        newCSS.minOutput = 0.
        newCSS.senNoiseStd = 0.00
        newCSS.nHat_B = CSSHat
        cssConstellation.appendCSS(newCSS)
    cssConstellation.outputConstellationMessage = "css_sensors_data"
    scSim.AddModelToTask(simTaskName, cssConstellation)
    # Add the normals to the vehicle Config data struct
    cssConstVehicle = fswMessages.CSSConfigFswMsg()
    totalCSSList = []
    for CSSHat in CSSOrientationList:
        newCSS = fswMessages.CSSUnitConfigFswMsg()
        newCSS.nHat_B = CSSHat
        newCSS.CBias = 1.0
        totalCSSList.append(newCSS)
    cssConstVehicle.nCSS = len(CSSOrientationList)
    cssConstVehicle.cssVals = totalCSSList

    # setup Sun Position
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'de430.bsp')  # solar system bodies
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'naif0011.tls')  # leap second file
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'de-403-masses.tpc')  # solar system masses
    pyswice.furnsh_c(gravFactory.spiceObject.SPICEDataPath + 'pck00010.tpc')  # generic Planetary Constants Kernel
    sunPositionMsg = simMessages.SpicePlanetStateSimMsg()
    sunInitialState = 1000 * pyswice.spkRead('SUN', timeInitString, 'J2000', 'EARTH')
    rN_sun = sunInitialState[0:3]  # meters
    vN_sun = sunInitialState[3:6]  # m/s
    sunPositionMsg.PositionVector = rN_sun
    sunPositionMsg.VelocityVector = vN_sun

    #
    #   setup the FSW algorithm tasks
    #

    inertial3DSpinConfig = inertial3DSpin.inertial3DSpinConfig()
    inertial3DSpinWrap = scSim.setModelDataWrap(inertial3DSpinConfig)
    inertial3DSpinWrap.ModelTag = "inertial3DSpin"
    scSim.AddModelToTask(simTaskName, inertial3DSpinWrap, inertial3DSpinConfig)
    inertial3DSpinConfig.outputDataName = "guidanceInertial3DSpin"
    inertial3DSpinConfig.omega_spin = np.array([0.0, 2.0, 0.0]) * macros.D2R
    inertial3DSpinConfig.inputRefName = "inertialSpinRef"
    RefStateOutData = inertial3DSpin.AttRefFswMsg()  # Create a structure for the input message
    inputMessageSize = RefStateOutData.getStructSize()
    scSim.TotalSim.CreateNewMessage(simProcessName,
                                          inertial3DSpinConfig.inputRefName,
                                          inputMessageSize,
                                          2)
    sigma_R0N = np.array([-1.0, 0.0, 0.0])
    RefStateOutData.sigma_RN = sigma_R0N
    omega_R0N_N = np.array([0.0, 0.0, 0.0])
    RefStateOutData.omega_RN_N = omega_R0N_N
    domega_R0N_N = np.array([0.0, 0.0, 0.0])
    RefStateOutData.domega_RN_N = domega_R0N_N
    scSim.TotalSim.WriteMessageData(inertial3DSpinConfig.inputRefName,
                                          inputMessageSize,
                                          0,
                                          RefStateOutData)


    # setup the attitude tracking error evaluation module
    attErrorConfig = attTrackingError.attTrackingErrorConfig()
    attErrorWrap = scSim.setModelDataWrap(attErrorConfig)
    attErrorWrap.ModelTag = "attErrorInertial3D"
    scSim.AddModelToTask(simTaskName, attErrorWrap, attErrorConfig)
    attErrorConfig.outputDataName = "attErrorInertial3DMsg"
    attErrorConfig.inputRefName = "guidanceInertial3DSpin"
    attErrorConfig.inputNavName = sNavObject.outputAttName

    # setup the QUAT PD control module
    quatControlConfig = QUAT_PD.QUAT_PDConfig()
    quatControlWrap = scSim.setModelDataWrap(quatControlConfig)
    quatControlWrap.ModelTag = "QUAT_PD"
    scSim.AddModelToTask(simTaskName, quatControlWrap, quatControlConfig)
    quatControlConfig.inputSunName = "sun_direction"
    quatControlConfig.inputAttName = sNavObject.outputAttName
    quatControlConfig.inputGuidName = attErrorConfig.outputDataName
    quatControlConfig.inputRatesName = ImuSensor.OutputDataMsg
    quatControlConfig.vehConfigInMsgName = "vehicleConfigName"
    quatControlConfig.outputDataName = "LrRequested"
    quatControlConfig.rwParamsInMsgName = "rwa_config_data_parsed"
    quatControlConfig.inputRWSpeedsName = rwStateEffector.OutputDataString
    quatControlConfig.outputErrorName = "controlError"
    quatControlConfig.K = 0.01
    quatControlConfig.P = 0.1



    # add module that maps the Lr control torque into the RW motor torques
    rwMotorTorqueConfig = rwMotorTorque.rwMotorTorqueConfig()
    rwMotorTorqueWrap = scSim.setModelDataWrap(rwMotorTorqueConfig)
    rwMotorTorqueWrap.ModelTag = "rwMotorTorque"
    scSim.AddModelToTask(simTaskName, rwMotorTorqueWrap, rwMotorTorqueConfig)
    # Initialize the test module msg names
    if useRWVoltageIO:
        rwMotorTorqueConfig.outputDataName = "rw_torque_Lr"
    else:
        rwMotorTorqueConfig.outputDataName = rwStateEffector.InputCmds
    rwMotorTorqueConfig.inputVehControlName = quatControlConfig.outputDataName
    rwMotorTorqueConfig.rwParamsInMsgName = quatControlConfig.rwParamsInMsgName
    # Make the RW control all three body axes
    controlAxes_B = [
        1, 0, 0, 0, 1, 0, 0, 0, 1
    ]
    rwMotorTorqueConfig.controlAxes_B = controlAxes_B

    if useRWVoltageIO:
        fswRWVoltageConfig = rwMotorVoltage.rwMotorVoltageConfig()
        fswRWVoltageWrap = scSim.setModelDataWrap(fswRWVoltageConfig)
        fswRWVoltageWrap.ModelTag = "rwMotorVoltage"

        # Add test module to runtime call list
        scSim.AddModelToTask(simTaskName, fswRWVoltageWrap, fswRWVoltageConfig)

        # Initialize the test module configuration data
        fswRWVoltageConfig.torqueInMsgName = rwMotorTorqueConfig.outputDataName
        fswRWVoltageConfig.rwParamsInMsgName = quatControlConfig.rwParamsInMsgName
        fswRWVoltageConfig.voltageOutMsgName = rwVoltageIO.rwVoltageInMsgName

        # set module parameters
        fswRWVoltageConfig.VMin = 0.0  # Volts
        fswRWVoltageConfig.VMax = 10.0  # Volts

    #
    #   Setup data logging before the simulation is initialized
    #
    numDataPoints = 100000
    samplingTime = simulationTime / (numDataPoints - 1)
    scSim.TotalSim.logThisMessage(cssConstellation.outputConstellationMessage, samplingTime)
    scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
    scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)
    scSim.TotalSim.logThisMessage(quatControlConfig.inputRWSpeedsName, samplingTime)
    scSim.TotalSim.logThisMessage(quatControlConfig.outputErrorName, samplingTime)
    scSim.TotalSim.logThisMessage(ImuSensor.OutputDataMsg, samplingTime)
    rwOutName = ["rw_config_0_data", "rw_config_1_data", "rw_config_2_data"]
    for item in rwOutName:
        scSim.TotalSim.logThisMessage(item, samplingTime)
    if useRWVoltageIO:
        scSim.TotalSim.logThisMessage(fswRWVoltageConfig.voltageOutMsgName, samplingTime)

    #
    # create simulation messages
    #

    # create the FSW vehicle configuration message
    vehicleConfigOut = fswMessages.VehicleConfigFswMsg()
    vehicleConfigOut.ISCPntB_B = I  # use the same inertia in the FSW algorithm as in the simulation
    unitTestSupport.setMessage(scSim.TotalSim,
                               simProcessName,
                               quatControlConfig.vehConfigInMsgName,
                               vehicleConfigOut)

    # FSW RW configuration message
    # use the same RW states in the FSW algorithm as in the simulation
    fswSetupRW.clearSetup()
    for key, rw in rwFactory.rwList.iteritems():
        fswSetupRW.create(unitTestSupport.EigenVector3d2np(rw.gsHat_B), rw.Js, 0.2)
    fswSetupRW.writeConfigMessage(quatControlConfig.rwParamsInMsgName, scSim.TotalSim, simProcessName)



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
    dataOmegaRW = scSim.pullMessageLogData(quatControlConfig.inputRWSpeedsName + ".wheelSpeeds", range(numRW))
    dataSigmaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".sigma_BN", range(3))
    dataOmegaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".omega_BN_B", range(3))
    dataSigmaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".sigma_BR", range(3))
    dataPRVAng = scSim.pullMessageLogData(quatControlConfig.outputErrorName + ".PRV_ang", range(1))
    dataImuRates = scSim.pullMessageLogData(ImuSensor.OutputDataMsg + ".AngVelPlatform", range(3))


    plt.figure(1)
    for idx in range(1,4):
        plt.plot(dataSigmaBR[:, 0] * macros.NANO2SEC, dataSigmaBR[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\sigma_' + str(idx) + '$',
                 linewidth=2)
    plt.legend(loc='lower right', fontsize=12)
    plt.xlabel('Time [min]', fontsize=12)
    plt.ylabel('Attitude Error $\sigma_{B/R}$')
    plt.title('Attitude Error', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(2)
    for idx in range(1, numRW + 1):
        plt.plot(dataOmegaRW[:, 0] * macros.NANO2SEC, dataOmegaRW[:, idx] / macros.RPM,
                 color=unitTestSupport.getLineColor(idx, numRW),
                 label='$\Omega_{' + str(idx) + '}$',
                 linewidth=2)
    plt.title('Reaction Wheel Rotation Speed', fontsize=12)
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('RW Speed [RPM]', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(3)
    for idx in range(1, 4):
        plt.plot(dataSigmaBN[:, 0] * macros.NANO2SEC, dataSigmaBN[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\sigma_' + str(idx) + '$',
                 linewidth=2)
    plt.title('Inertial Attitude MRPs', fontsize=12)
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('$\sigma_{B/N}$', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(4)
    for idx in range(1, 4):
        plt.plot(dataOmegaBN[:, 0] * macros.NANO2SEC, dataOmegaBN[:, idx]*macros.R2D,
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\omega_' + str(idx) + '$',
                 linewidth=2)
    plt.title('Spacecraft Angular Rates', fontsize=12)
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Angular Rates [deg/s]', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(5)
    fig = plt.gcf()
    ax = fig.gca()
    vectorData = unitTestSupport.pullVectorSetFromData(dataSigmaBR)
    sNorm = np.array([np.linalg.norm(v) for v in vectorData])
    plt.plot(dataSigmaBR[:,0] * macros.NANO2SEC, sNorm,
             color=unitTestSupport.getLineColor(1, 3),
                 linewidth=2)
    plt.title('Norm of the Attitude Error', fontsize=12)
    plt.xlabel('Time [min]', fontsize=12)
    plt.ylabel('Attitude Error Norm $|\sigma_{B/R}|$', fontsize=12)
    ax.set_yscale('log')
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(6)
    for idx in range(1, 4):
        plt.plot(dataImuRates[:, 0] * macros.NANO2SEC, dataImuRates[:, idx] * macros.R2D,
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\omega_' + str(idx) + '$',
                 linewidth=2)
    plt.title('IMU Angular Rate Output', fontsize=12)
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Angular Rates [deg/s]', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    plt.figure(7)
    plt.plot(dataPRVAng[:, 0] * macros.NANO2SEC, dataPRVAng[:, 1] * macros.R2D,
             color=unitTestSupport.getLineColor(1, 1),
             label='$\\theta$',
             linewidth=2)
    p15d = plt.axhline(y=3, color='r', linestyle='--', linewidth=2)
    n15d = plt.axhline(y=-3, color='r', linestyle='--', linewidth=2)
    plt.legend((p15d, n15d), ('+ 3 deg', '- 3 deg'), loc='upper right', fontsize=12)
    plt.title('Control Error Angle', fontsize=12)
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Angle [$\\theta$]', fontsize=12)
    plt.tick_params(labelsize=12)
    plt.grid(True)

    if show_plots:
        plt.show()

    # close the plots being saved off to avoid over-writing old and new figures
    plt.close("all")

    return dataSigmaBR, numDataPoints


#
# This statement below ensures that the unit test scrip can be run as a
# stand-along python script
#
if __name__ == "__main__":
    run(
        True,   # show_plots
        False,   # useUnmodeledTorque
        False,  # useJitterSimple
        False   # useRWVoltageIO
    )