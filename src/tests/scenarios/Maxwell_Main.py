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
# Purpose:  Integrated test of the spacecraftPlus(), extForceTorque, simpleNav() and
#           MRP_Feedback() modules.  Illustrates a 6-DOV spacecraft detumbling in orbit.
#           This scenario is the same as scenarioAttitudeControl, but with the
#           difference that here the control and dynamics are executed at different
#           frequencies or time steps.
# Author:   Hanspeter Schaub
# Creation Date:  Nov. 25, 2016
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

# import simulation related support
from Basilisk.simulation import spacecraftPlus
from Basilisk.simulation import extForceTorque
from Basilisk.simulation import simMessages
from Basilisk.simulation import sim_model
from Basilisk.simulation import simple_nav
from Basilisk.simulation import mag_meter
from Basilisk.simulation import imu_sensor
from Basilisk.simulation import coarse_sun_sensor
from Basilisk.simulation import reactionWheelStateEffector
from Basilisk.simulation import rwVoltageInterface
from Basilisk.simulation import torqueRodDynamicEffector

# import FSW Algorithm related support
from Basilisk.fswAlgorithms import B_DOT
from Basilisk.fswAlgorithms import inertial3D
from Basilisk.fswAlgorithms import attTrackingError
from Basilisk.fswAlgorithms import rwMotorVoltage
from Basilisk.fswAlgorithms import rwMotorTorque
from Basilisk.fswAlgorithms import maxwellLS
from Basilisk.fswAlgorithms import QUAT_PD
from Basilisk.fswAlgorithms import sunSafePoint


# import message declarations
from Basilisk.fswAlgorithms import fswMessages
bskPath = __path__[0]
from Basilisk import pyswice

def run(show_plots, detumble, saturate, sunpoint, useUnmodeledTorque, useJitterSimple, useRWVoltageIO):
    '''Call this routine directly to run the tutorial scenario.'''

    # Create simulation variable names
    dynTaskName = "dynTask"
    dynProcessName = "dynProcess"

    fswTaskName = "fswTask"
    fswProcessName = "fswProcess"

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()
    scSim.TotalSim.terminateSimulation()

    # set the simulation time variable used later on
    simulationTime = macros.min2nano(2)

    #
    #  create the simulation process
    #
    dynProcess = scSim.CreateNewProcess(dynProcessName)
    fswProcess = scSim.CreateNewProcess(fswProcessName)

    # Process message interfaces.
    # this step is used to copy messages between the dyn and fsw processes
    # as long as the message has the same name, it will get copied over automatically
    dyn2FSWInterface = sim_model.SysInterface()
    fsw2DynInterface = sim_model.SysInterface()

    dyn2FSWInterface.addNewInterface(dynProcessName, fswProcessName)
    fsw2DynInterface.addNewInterface(fswProcessName, dynProcessName)

    fswProcess.addInterfaceRef(dyn2FSWInterface)
    dynProcess.addInterfaceRef(fsw2DynInterface)

    # create the dynamics task and specify the integration update time
    simTimeStep = macros.sec2nano(0.1)
    dynProcess.addTask(scSim.CreateNewTask(dynTaskName, simTimeStep))
    fswTimeStep = macros.sec2nano(0.1)
    fswProcess.addTask(scSim.CreateNewTask(fswTaskName, fswTimeStep))

    # if this scenario is to interface with the BSK Viz, uncomment the following lines
    # unitTestSupport.enableVisualization(scSim, dynProcess, simProcessName, 'earth')  # The Viz only support 'earth', 'mars', or 'sun'

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
    scSim.AddModelToTask(dynTaskName, scObject)

    # clear prior gravitational body and SPICE setup definitions
    gravFactory = simIncludeGravBody.gravBodyFactory()
    gravBodies = gravFactory.createBodies(['earth','sun','moon'])


    # setup Earth Gravity Body
    earth =  gravBodies['earth']
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
    scSim.AddModelToTask(dynTaskName, gravFactory.spiceObject, None, -1)
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
    oe.i = 45 * macros.D2R
    oe.Omega = 0.0 * macros.D2R
    oe.omega = 0.0 * macros.D2R
    oe.f = 180.0 * macros.D2R
    rN, vN = orbitalMotion.elem2rv(mu, oe)
    scObject.hub.r_CN_NInit = unitTestSupport.np2EigenVectorXd(rN)  # m   - r_CN_N
    scObject.hub.v_CN_NInit = unitTestSupport.np2EigenVectorXd(vN)  # m/s - v_CN_N
    scObject.hub.sigma_BNInit = [[0.1], [0.2], [-0.3]]  # sigma_BN_B
    if detumble:
        scObject.hub.omega_BN_BInit = [[13*macros.D2R], [13*macros.D2R], [13*macros.D2R]]  # rad/s - omega_BN_B
    if sunpoint:
        scObject.hub.omega_BN_BInit = [[0.001*macros.D2R], [0.001*macros.D2R], [0.001*macros.D2R]]  # rad/s - omega_BN_B

    if saturate or sunpoint:
        #
        # Add RW devices
        #
        rwFactory = simIncludeRW.rwFactory()

        # store the RW dynamical model type
        varRWModel = rwFactory.BalancedWheels
        if useJitterSimple:
            varRWModel = rwFactory.JitterSimple

        # create each RW by specifying the RW type, the spin axis gsHat, plus optional arguments
        RW1 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0.906307787036650, 0], maxMomentum=0.02, Omega=0.  # RPM
                               , RWModel=varRWModel,
                               )
        RW2 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0, 0.906307787036650], maxMomentum=0.02, Omega=0.  # RPM
                               , RWModel=varRWModel,
                               )
        RW3 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, -0.906307787036650, 0], maxMomentum=0.02, Omega=0.  # RPM
                               , RWModel=varRWModel,
                               )
        RW4 = rwFactory.create('NanoAvionics_RW0', [0.422618261740699, 0, -0.906307787036650], maxMomentum=0.02, Omega=0.
                               , RWModel=varRWModel,
                               )

        numRW = rwFactory.getNumOfDevices()

        # create RW object container and tie to spacecraft object
        rwStateEffector = reactionWheelStateEffector.ReactionWheelStateEffector()
        rwStateEffector.InputCmds = "reactionwheel_cmds"
        rwFactory.addToSpacecraft("ReactionWheels", rwStateEffector, scObject)

        # add RW object array to the simulation process
        scSim.AddModelToTask(dynTaskName, rwStateEffector, None, 2)

        if useRWVoltageIO:
            rwVoltageIO = rwVoltageInterface.RWVoltageInterface()
            rwVoltageIO.ModelTag = "rwVoltageInterface"

            # set module parameters(s)
            rwVoltageIO.setGains(np.array([0.2 / 10.] * 3))  # [Nm/V] conversion gain

            # Add test module to runtime call list
            scSim.AddModelToTask(dynTaskName, rwVoltageIO)


    # add the simple Navigation sensor module.  This sets the SC attitude, rate, position
    # velocity navigation message
    sNavObject = simple_nav.SimpleNav()
    sNavObject.ModelTag = "SimpleNavigation"
    scSim.AddModelToTask(dynTaskName, sNavObject)

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
    gyroNoise = 0.000  # Noise

    ImuSensor.setLSBs(accelLSBIn, gyroLSBIn)
    ImuSensor.senRotBias = np.array([senRotBiasIn] * 3)
    ImuSensor.senRotMax = senRotMaxIn
    ImuSensor.gyroScale = np.array(gyroScale)
    ImuSensor.PMatrixGyro = np.eye(3) * gyroNoise
    ImuSensor.walkBoundsGyro = np.array(errorBoundsGryo)

    # add IMU to Simulation Process
    scSim.AddModelToTask(dynTaskName, ImuSensor)

    # Add Mag Meter
    MagMeter = mag_meter.MagMeter()
    MagMeter.ModelTag = "MagMeter"
    MagMeterNoise = 0.00000
    MagMeterBias = 0.0000
    ImuSensor.senRotBias = np.array([MagMeterBias] * 3)
    MagMeter.PMatrix = np.eye(3) * MagMeterNoise
    MagMeter.inclination = oe.i
    MagMeter.orbitRadius = oe.a / 1000  # 6371.0 + orbitRadius
    scSim.AddModelToTask(dynTaskName, MagMeter)

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

    for CSSHat in CSSOrientationList:
        newCSS = coarse_sun_sensor.CoarseSunSensor()
        newCSS.minOutput = 0.
        newCSS.senNoiseStd = 0.00
        newCSS.nHat_B = CSSHat
        cssConstellation.appendCSS(newCSS)
    cssConstellation.outputConstellationMessage = "css_sensors_data"
    scSim.AddModelToTask(dynTaskName, cssConstellation)
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

    # setup inertial3D guidance module
    inertial3DConfig = inertial3D.inertial3DConfig()
    inertial3DWrap = scSim.setModelDataWrap(inertial3DConfig)
    inertial3DWrap.ModelTag = "inertial3D"
    scSim.AddModelToTask(fswTaskName, inertial3DWrap, inertial3DConfig)
    inertial3DConfig.sigma_R0N = [0., 0., 0.]  # set the desired inertial orientation
    inertial3DConfig.outputDataName = "guidanceInertial3D"

    # setup the attitude tracking error evaluation module
    attErrorConfig = attTrackingError.attTrackingErrorConfig()
    attErrorWrap = scSim.setModelDataWrap(attErrorConfig)
    attErrorWrap.ModelTag = "attErrorInertial3D"
    scSim.AddModelToTask(fswTaskName, attErrorWrap, attErrorConfig)
    attErrorConfig.outputDataName = "attErrorInertial3DMsg"
    attErrorConfig.inputRefName = inertial3DConfig.outputDataName
    attErrorConfig.inputNavName = sNavObject.outputAttName

    if detumble:
        # setup the MRP Feedback control module
        bdotControlConfig = B_DOT.B_DOTConfig()
        bdotControlWrap = scSim.setModelDataWrap(bdotControlConfig)
        bdotControlWrap.ModelTag = "B_DOT"
        scSim.AddModelToTask(fswTaskName, bdotControlWrap, bdotControlConfig)
        bdotControlConfig.inputMagMeterName = MagMeter.outputStateMessage
        bdotControlConfig.vehConfigInMsgName = "vehicleConfigName"
        bdotControlConfig.outputDataName = "LrRequested"
        bdotControlConfig.K_detumble = 1000.0

        if saturate:
            bdotControlConfig.use_rw_wheels = 1
            bdotControlConfig.rwParamsInMsgName = "rwa_config_data_parsed"
            bdotControlConfig.inputRWSpeedsName = rwStateEffector.OutputDataString
            # add module that maps the Lr control torque into the RW motor torques
            rwMotorTorqueConfig = rwMotorTorque.rwMotorTorqueConfig()
            rwMotorTorqueWrap = scSim.setModelDataWrap(rwMotorTorqueConfig)
            rwMotorTorqueWrap.ModelTag = "rwMotorTorque"
            scSim.AddModelToTask(dynTaskName, rwMotorTorqueWrap, rwMotorTorqueConfig)
            # Initialize the test module msg names
            if useRWVoltageIO:
                rwMotorTorqueConfig.outputDataName = "rw_torque_Lr"
            else:
                rwMotorTorqueConfig.outputDataName = rwStateEffector.InputCmds
            rwMotorTorqueConfig.inputVehControlName = bdotControlConfig.outputDataName
            rwMotorTorqueConfig.rwParamsInMsgName = bdotControlConfig.rwParamsInMsgName
            # Make the RW control all three body axes
            controlAxes_B = [
                1, 0, 0,
                0, 1, 0,
                0, 0, 1
            ]
            rwMotorTorqueConfig.controlAxes_B = controlAxes_B

            if useRWVoltageIO:
                fswRWVoltageConfig = rwMotorVoltage.rwMotorVoltageConfig()
                fswRWVoltageWrap = scSim.setModelDataWrap(fswRWVoltageConfig)
                fswRWVoltageWrap.ModelTag = "rwMotorVoltage"

                # Add test module to runtime call list
                scSim.AddModelToTask(dynTaskName, fswRWVoltageWrap, fswRWVoltageConfig)

                # Initialize the test module configuration data
                fswRWVoltageConfig.torqueInMsgName = rwMotorTorqueConfig.outputDataName
                fswRWVoltageConfig.rwParamsInMsgName = bdotControlConfig.rwParamsInMsgName
                fswRWVoltageConfig.voltageOutMsgName = rwVoltageIO.rwVoltageInMsgName

                # set module parameters
                fswRWVoltageConfig.VMin = 0.0  # Volts
                fswRWVoltageConfig.VMax = 5.0  # Volts
        else:
            bdotControlConfig.use_rw_wheels = 0
            torqueRodConfig = torqueRodDynamicEffector.torqueRodDynamicEffector()
            # torqueRodWrap = scSim.setModelDataWrap(torqueRodConfig)
            torqueRodConfig.ModelTag = "torqueRods"
            torqueRodConfig.magFieldMsgName = MagMeter.outputStateMessage
            torqueRodConfig.cmdTorqueRodsMsgName = bdotControlConfig.outputDataName
            torqueRodConfig.MaxDipoleMoment = 0.11  # [Am^2]
            scObject.addDynamicEffector(torqueRodConfig)
            scSim.AddModelToTask(dynTaskName, torqueRodConfig)

    if sunpoint:
        # Add Maxwell LS
        sunVectorConfig = maxwellLS.maxwellLSConfig()
        sunVectorWrap = scSim.setModelDataWrap(sunVectorConfig)
        sunVectorWrap.ModelTag = "maxwellLS"
        sunVectorConfig.cssDataInMsgName = "css_sensors_data"
        sunVectorConfig.cssConfigInMsgName = "css_config_data"
        sunVectorConfig.navStateOutMsgName = "css_nav_sunHeading"
        sunVectorConfig.sunpointOutMsgName = "sun_direction"
        sunVectorConfig.sensorUseThresh = 0.15
        scSim.AddModelToTask(fswTaskName, sunVectorWrap, sunVectorConfig)

        # setup the QUAT PD control module
        quatControlConfig = QUAT_PD.QUAT_PDConfig()
        quatControlWrap = scSim.setModelDataWrap(quatControlConfig)
        quatControlWrap.ModelTag = "QUAT_PD"
        scSim.AddModelToTask(fswTaskName, quatControlWrap, quatControlConfig)
        quatControlConfig.inputSunName = "sun_direction"
        quatControlConfig.inputAttName = sNavObject.outputAttName
        quatControlConfig.inputGuidName = attErrorConfig.outputDataName
        quatControlConfig.inputRatesName = ImuSensor.OutputDataMsg
        quatControlConfig.vehConfigInMsgName = "vehicleConfigName"
        quatControlConfig.outputDataName = "LrRequested"
        quatControlConfig.rwParamsInMsgName = "rwa_config_data_parsed"
        quatControlConfig.inputRWSpeedsName = rwStateEffector.OutputDataString
        quatControlConfig.outputErrorName = "controlError"
        quatControlConfig.K = 0.015
        quatControlConfig.P = 0.01

        # add module that maps the Lr control torque into the RW motor torques
        rwMotorTorqueConfig = rwMotorTorque.rwMotorTorqueConfig()
        rwMotorTorqueWrap = scSim.setModelDataWrap(rwMotorTorqueConfig)
        rwMotorTorqueWrap.ModelTag = "rwMotorTorque"
        scSim.AddModelToTask(dynTaskName, rwMotorTorqueWrap, rwMotorTorqueConfig)
        # Initialize the test module msg names
        if useRWVoltageIO:
            rwMotorTorqueConfig.outputDataName = "rw_torque_Lr"
        else:
            rwMotorTorqueConfig.outputDataName = rwStateEffector.InputCmds
        rwMotorTorqueConfig.inputVehControlName = quatControlConfig.outputDataName
        rwMotorTorqueConfig.rwParamsInMsgName = quatControlConfig.rwParamsInMsgName
        # Make the RW control all three body axes
        controlAxes_B = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]
        rwMotorTorqueConfig.controlAxes_B = controlAxes_B

        if useRWVoltageIO:
            fswRWVoltageConfig = rwMotorVoltage.rwMotorVoltageConfig()
            fswRWVoltageWrap = scSim.setModelDataWrap(fswRWVoltageConfig)
            fswRWVoltageWrap.ModelTag = "rwMotorVoltage"

            # Add test module to runtime call list
            scSim.AddModelToTask(dynTaskName, fswRWVoltageWrap, fswRWVoltageConfig)

            # Initialize the test module configuration data
            fswRWVoltageConfig.torqueInMsgName = rwMotorTorqueConfig.outputDataName
            fswRWVoltageConfig.rwParamsInMsgName = quatControlConfig.rwParamsInMsgName
            fswRWVoltageConfig.voltageOutMsgName = rwVoltageIO.rwVoltageInMsgName

            # set module parameters
            fswRWVoltageConfig.VMin = 0.0  # Volts
            fswRWVoltageConfig.VMax = 5.0  # Volts


    #
    #   Setup data logging before the simulation is initialized
    #
    numDataPoints = 100000
    samplingTime = simulationTime / (numDataPoints - 1)
    if detumble:
        # scSim.TotalSim.logThisMessage(bdotControlConfig.outputDataName, samplingTime)
        # scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
        # scSim.TotalSim.logThisMessage(sNavObject.outputTransName, samplingTime)
        # scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)
        scSim.TotalSim.logThisMessage(ImuSensor.OutputDataMsg, samplingTime)
        scSim.TotalSim.logThisMessage(MagMeter.outputStateMessage, samplingTime)
        scSim.TotalSim.logThisMessage(bdotControlConfig.inputMagMeterName, samplingTime)

        # create the FSW vehicle configuration message
        vehicleConfigOut = fswMessages.VehicleConfigFswMsg()
        vehicleConfigOut.ISCPntB_B = I  # use the same inertia in the FSW algorithm as in the simulation
        unitTestSupport.setMessage(scSim.TotalSim,
                                   fswProcessName,
                                   bdotControlConfig.vehConfigInMsgName,
                                   vehicleConfigOut)
        if saturate:
            scSim.TotalSim.logThisMessage(bdotControlConfig.inputRWSpeedsName, samplingTime)
            rwOutName = ["rw_config_0_data", "rw_config_1_data", "rw_config_2_data", "rw_config_3_data"]
            for item in rwOutName:
                scSim.TotalSim.logThisMessage(item, samplingTime)
            if useRWVoltageIO:
                scSim.TotalSim.logThisMessage(fswRWVoltageConfig.voltageOutMsgName, samplingTime)

            # FSW RW configuration message
            # use the same RW states in the FSW algorithm as in the simulation
            fswSetupRW.clearSetup()
            for key, rw in rwFactory.rwList.iteritems():
                fswSetupRW.create(unitTestSupport.EigenVector3d2np(rw.gsHat_B), rw.Js, 0.2)
            fswSetupRW.writeConfigMessage(bdotControlConfig.rwParamsInMsgName, scSim.TotalSim, dynProcessName)

    if sunpoint:
        scSim.TotalSim.logThisMessage(cssConstellation.outputConstellationMessage, samplingTime)
        scSim.TotalSim.logThisMessage(sunVectorConfig.sunpointOutMsgName, samplingTime)
        scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
        scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)
        scSim.TotalSim.logThisMessage(quatControlConfig.inputRWSpeedsName, samplingTime)
        scSim.TotalSim.logThisMessage(quatControlConfig.outputErrorName, samplingTime)
        scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
        rwOutName = ["rw_config_0_data", "rw_config_1_data", "rw_config_2_data", "rw_config_3_data"]
        for item in rwOutName:
            scSim.TotalSim.logThisMessage(item, samplingTime)
        if useRWVoltageIO:
            scSim.TotalSim.logThisMessage(fswRWVoltageConfig.voltageOutMsgName, samplingTime)

        # create the FSW vehicle configuration message
        vehicleConfigOut = fswMessages.VehicleConfigFswMsg()
        vehicleConfigOut.ISCPntB_B = I  # use the same inertia in the FSW algorithm as in the simulation
        unitTestSupport.setMessage(scSim.TotalSim,
                                   fswProcessName,
                                   quatControlConfig.vehConfigInMsgName,
                                   vehicleConfigOut)

        # FSW RW configuration message
        # use the same RW states in the FSW algorithm as in the simulation
        fswSetupRW.clearSetup()
        for key, rw in rwFactory.rwList.iteritems():
            fswSetupRW.create(unitTestSupport.EigenVector3d2np(rw.gsHat_B), rw.Js, 0.2)
        fswSetupRW.writeConfigMessage(quatControlConfig.rwParamsInMsgName, scSim.TotalSim, dynProcessName)


    #
    #   initialize Simulation
    #
    scSim.InitializeSimulationAndDiscover()

    # this next call ensures that the FSW and Dynamics Message that have the same
    # name are copied over every time the simulation ticks forward.  This function
    # has to be called after the simulation is initialized to ensure that all modules
    # have created their own output/input messages declarations.
    # dyn2FSWInterface.discoverAllMessages()
    # fsw2DynInterface.discoverAllMessages()

    #
    #   configure a simulation stop time time and execute the simulation run
    #
    scSim.ConfigureStopTime(simulationTime)
    scSim.ExecuteSimulation()

    #
    #   retrieve the logged data
    #
    if detumble:
        # dataLr = scSim.pullMessageLogData(bdotControlConfig.outputDataName + ".torqueRequestBody", range(3))
        # dataPos = scSim.pullMessageLogData(sNavObject.outputTransName + ".r_BN_N", range(3))
        dataOmegaIMU = scSim.pullMessageLogData(ImuSensor.OutputDataMsg + ".AngVelPlatform", range(3))
        dataMagBody = scSim.pullMessageLogData(bdotControlConfig.inputMagMeterName + ".mag_bf", range(3))
        dataMagLVLH = scSim.pullMessageLogData(bdotControlConfig.inputMagMeterName + ".mag_hill", range(3))

        if saturate:
            dataOmegaRW = scSim.pullMessageLogData(bdotControlConfig.inputRWSpeedsName + ".wheelSpeeds", range(numRW))
    np.set_printoptions(precision=16)

    if sunpoint:
        dataCSSArray = scSim.pullMessageLogData(cssConstellation.outputConstellationMessage + ".CosValue",
                                                range(len(CSSOrientationList)))
        dataSunVector = scSim.pullMessageLogData(sunVectorConfig.sunpointOutMsgName + ".q_des_RN", range(4))
        dataOmegaRW = scSim.pullMessageLogData(quatControlConfig.inputRWSpeedsName + ".wheelSpeeds", range(numRW))
        dataSigmaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".sigma_BN", range(3))
        dataOmegaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".omega_BN_B", range(3))
        dataSigmaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".sigma_BR", range(3))
    #
    #   plot the results
    #
    fileName = os.path.basename(os.path.splitext(__file__)[0])
    plt.close("all")  # clears out plots from earlier test runs
    if detumble:
        plt.figure(1)
        for idx in range(1, 4):
            plt.plot(dataOmegaIMU[:, 0] * macros.NANO2MIN, dataOmegaIMU[:, idx] * macros.R2D,
                     color=unitTestSupport.getLineColor(idx, 3),
                     label='$\omega_' + str(idx) + '$')
        plt.title('Detumbling Simulation Angular Rates', fontsize=16, fontweight='bold')
        plt.legend(loc='upper right', fontsize=16)
        plt.xlabel('Time (min)', fontsize=16)
        plt.ylabel('Angular Rates (deg/s)', fontsize=16)

        # # Mag Meter Body
        # plt.figure(6)
        # plt.plot(dataMagBody[:, 0] * macros.NANO2HOUR, dataMagBody[:, 1],
        #          color='blue',
        #          label='x')
        # plt.plot(dataMagBody[:, 0] * macros.NANO2HOUR, dataMagBody[:, 2],
        #          color='red',
        #          label='y')
        # plt.plot(dataMagBody[:, 0] * macros.NANO2HOUR, dataMagBody[:, 3],
        #          color='black',
        #          label='z')
        # plt.grid(True)
        # plt.legend(loc='upper right', fontsize=16)
        # plt.title('Magnetic Field - Body Frame', fontsize=16)
        # plt.xlabel('Time (h)', fontsize=16)
        # plt.ylabel('Magnetic Field Magnitude (T)', fontsize=16)

        # # Mag Meter LVLH
        # plt.figure(7)
        # plt.plot(dataMagLVLH[:, 0] * macros.NANO2HOUR, dataMagLVLH[:, 1],
        #         color='blue',
        #         label='$i_r$')
        # plt.plot(dataMagLVLH[:, 0] * macros.NANO2HOUR, dataMagLVLH[:, 2],
        #          color='red',
        #          label='$i_{\\theta}$')
        # plt.plot(dataMagLVLH[:, 0] * macros.NANO2HOUR, dataMagLVLH[:, 3],
        #          color='black',
        #          label='$i_h$')
        # plt.grid(True)
        # plt.legend(loc='upper right', fontsize=16)
        # plt.title('Basilisk (Simple Tilted Dipole) - 90 degree inclination', fontsize=16)
        # plt.xlabel('Time (h)', fontsize=16)
        # plt.ylabel('Magnetic Field Magnitude (T)', fontsize=16)

        if saturate:
            plt.figure(2)
            for idx in range(1, numRW + 1):
                plt.plot(dataOmegaRW[:, 0] * macros.NANO2MIN, dataOmegaRW[:, idx] / macros.RPM,
                         color=unitTestSupport.getLineColor(idx, numRW),
                         label='$\Omega_{' + str(idx) + '}$')
            plt.title('Reaction Wheel Spin Rates', fontsize=16, fontweight='bold')
            plt.legend(loc='upper right', fontsize=16)
            plt.xlabel('Time (min)', fontsize=16)
            plt.ylabel('RW Speed [RPM]', fontsize=16)

    if sunpoint:
        # CSS Sensor Readings
        plt.figure(1)
        for idx in range(1, 15):  # range(1,len(CSSList)+1) currently hardcoded. Remove when initialization block
            plt.plot(dataCSSArray[:, 0] * macros.NANO2SEC, dataCSSArray[:, idx],
                     # color=unitTestSupport.getLineColor(idx,2),
                     label='CSS$_{' + str(idx) + '}$')
        plt.title('CSS raw sensor readings', fontsize=12, fontweight='bold')
        plt.xlabel('Time [sec]', fontsize=10, fontweight='bold')
        plt.legend(fontsize=10)
        plt.ylabel("CSS Voltage", fontsize=10, fontweight='bold')

        # plt.figure(2)
        # for idx in range(1, 5):
        #     plt.plot(dataSunVector[:, 0] * macros.NANO2SEC, dataSunVector[:, idx],
        #              color=unitTestSupport.getLineColor(idx, 4),
        #              label='$\\beta_{' + str(idx) + '}$')
        # plt.legend(loc='lower right')
        # plt.title('Sun Vector Estimation Quaternion')
        # plt.xlabel('Time [sec]')
        # plt.ylabel('Quaternion $\\beta_{B/R}$')

        plt.figure(7)
        for idx in range(1, 4):
            plt.plot(dataSigmaBR[:, 0] * macros.NANO2SEC, dataSigmaBR[:, idx],
                     color=unitTestSupport.getLineColor(idx, 3),
                     label='$\sigma_' + str(idx) + '$')
        plt.title('Control Error', fontsize=16, fontweight='bold')
        plt.legend(loc='upper right', fontsize=16)
        plt.xlabel('Time (s)', fontsize=16)
        plt.ylabel('$\sigma_{B/R}$', fontsize=16)

        plt.figure(4)
        for idx in range(1, numRW + 1):
            plt.plot(dataOmegaRW[:, 0] * macros.NANO2SEC, dataOmegaRW[:, idx] / macros.RPM,
                     color=unitTestSupport.getLineColor(idx, numRW),
                     label='$\Omega_{' + str(idx) + '}$')
        plt.legend(loc='lower right')
        plt.xlabel('Time [sec]')
        plt.ylabel('RW Speed (RPM) ')

        # plt.figure(5)
        # for idx in range(1,4):
        #     plt.plot(dataSigmaBN[:, 0] * macros.NANO2SEC, dataSigmaBN[:, idx],
        #              color=unitTestSupport.getLineColor(idx, 3),
        #              label='$\sigma_' + str(idx) + '$')
        # plt.legend(loc='lower right')
        # plt.xlabel('Time [min]')
        # plt.ylabel('Inertial Attitude $\sigma_{B/N}$')

        plt.figure(6)
        for idx in range(1,4):
            plt.plot(dataOmegaBN[:, 0] * macros.NANO2SEC, dataOmegaBN[:, idx] * macros.R2D,
                     color=unitTestSupport.getLineColor(idx, 3),
                     label='$\omega_' + str(idx) + '$')
        plt.legend(loc='lower right')
        plt.xlabel('Time [sec]')
        plt.ylabel('Angular Rates')

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
        True,   # show_plots
        False,   # detumble
        False,  # saturate
        True,  # sunpoint
        False,  # useUnmodeledTorque
        False,  # useJitterSimple
        False,  # useRWVoltageIO
        )
