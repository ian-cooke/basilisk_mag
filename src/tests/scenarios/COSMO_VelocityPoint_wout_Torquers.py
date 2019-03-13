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
from Basilisk.fswAlgorithms import velocityPoint


# import FSW Algorithm related support
from Basilisk.fswAlgorithms import inertial3D
from Basilisk.fswAlgorithms import attTrackingError
from Basilisk.fswAlgorithms import MRP_Feedback
from Basilisk.fswAlgorithms import rwMotorVoltage
from Basilisk.fswAlgorithms import rwMotorTorque
from Basilisk.fswAlgorithms import maxwellLS
from Basilisk.fswAlgorithms import B_DOT
from Basilisk.fswAlgorithms import cssWlsEst
from Basilisk.fswAlgorithms import sunSafePoint


# import message declarations
from Basilisk.fswAlgorithms import fswMessages
bskPath = __path__[0]
from Basilisk import pyswice


def plot_track_error_norm(timeLineSet, dataSigmaBR):
    plt.figure(1)
    fig = plt.gcf()
    ax = fig.gca()
    vectorData = unitTestSupport.pullVectorSetFromData(dataSigmaBR)
    sNorm = np.array([np.linalg.norm(v) for v in vectorData])
    plt.plot(timeLineSet, sNorm,
             color=unitTestSupport.getLineColor(1, 3),
             )
    plt.xlabel('Time [min]')
    plt.ylabel('Attitude Error Norm $|\sigma_{B/R}|$')
    ax.set_yscale('log')


def plot_control_torque(timeLineSet, dataLr):
    plt.figure(2)
    for idx in range(1, 4):
        plt.plot(timeLineSet, dataLr[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$L_{r,' + str(idx) + '}$')
    plt.legend(loc='lower right')
    plt.xlabel('Time [min]')
    plt.ylabel('Control Torque $L_r$ [Nm]')


def plot_rate_error(timeLineSet, dataOmegaBR):
    plt.figure(3)
    for idx in range(1, 4):
        plt.plot(timeLineSet, macros.R2D * dataOmegaBR[:, idx],
                 color=unitTestSupport.getLineColor(idx, 3),
                 label='$\omega_{BR,' + str(idx) + '}$')
    plt.legend(loc='lower right')
    plt.xlabel('Time [min]')
    plt.ylabel('Rate Tracking Error [rad/s] ')


def plot_orbit(oe, mu, planet_radius, dataPos, dataVel):
    # draw orbit in perifocal frame
    p = oe.a * (1 - oe.e * oe.e)
    plt.figure(4, figsize=np.array((1.0, 1.)) * 4.75, dpi=100)
    # draw the planet
    fig = plt.gcf()
    ax = fig.gca()
    planetColor = '#008800'
    # planet = gravFactory.createEarth()
    planetRadius = planet_radius / 1000
    ax.add_artist(plt.Circle((0, 0), planetRadius, color=planetColor))
    # draw the actual orbit
    rData = []
    fData = []
    for idx in range(0, len(dataPos)):
        oeData = orbitalMotion.rv2elem(mu, dataPos[idx, 1:4], dataVel[idx, 1:4])
        rData.append(oeData.rmag)
        fData.append(oeData.f + oeData.omega - oe.omega)
    plt.plot(rData * np.cos(fData) / 1000, rData * np.sin(fData) / 1000,
             color='#aa0000', linewidth=3.0, label='Simulated Flight')

    plt.axis(np.array([-1, 1, -1, 1]) * 1.25 * np.amax(rData) / 1000)

    # draw the full osculating orbit from the initial conditions
    tempAngle = (1. / 2.) * (np.pi - 2 * np.arcsin(1 / oe.e)) * 1.01
    fData = np.linspace(np.pi - tempAngle, -np.pi + tempAngle, 100)
    rData = []
    for idx in range(0, len(fData)):
        rData.append(p / (1 + oe.e * np.cos(fData[idx])))
    plt.plot(rData * np.cos(fData) / 1000, rData * np.sin(fData) / 1000, '--', color='#555555', label='Orbit Track')
    plt.xlabel('$i_e$ Cord. [km]')
    plt.ylabel('$i_p$ Cord. [km]')
    plt.legend(loc='lower left')
    plt.grid()


def run(show_plots):
    '''Call this routine directly to run the tutorial scenario.'''

    # Create simulation variable names
    simTaskName = "simTask"
    simProcessName = "simProcess"

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()
    scSim.TotalSim.terminateSimulation()

    # set the simulation time variable used later on
    simulationTime = macros.min2nano(180)

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
    I = [0.02, 0., 0.,
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
    rN_sun = sunInitialState[0:3]  # meters
    vN_sun = sunInitialState[3:6]  # m/s
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
    oe.i = 0 * macros.D2R
    oe.Omega = 0.0 * macros.D2R
    oe.omega = 0.0 * macros.D2R
    oe.f = 180.0 * macros.D2R
    rN, vN = orbitalMotion.elem2rv(mu, oe)
    scObject.hub.r_CN_NInit = unitTestSupport.np2EigenVectorXd(rN)  # m   - r_CN_N
    scObject.hub.v_CN_NInit = unitTestSupport.np2EigenVectorXd(vN)  # m/s - v_CN_N
    scObject.hub.sigma_BNInit = [[0], [0], [0.4142]]  # sigma_BN_B
    scObject.hub.omega_BN_BInit = [[0. * macros.D2R], [0. * macros.D2R], [0. * macros.D2R]]  # rad/s - omega_CN_B

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
    scSim.AddModelToTask(simTaskName, sNavObject)

    # setup velocityPoint guidance module
    attGuidanceConfig = velocityPoint.velocityPointConfig()
    attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
    attGuidanceWrap.ModelTag = "velocityPoint"
    attGuidanceConfig.inputNavDataName = sNavObject.outputTransName
    attGuidanceConfig.inputCelMessName = earth.bodyInMsgName
    attGuidanceConfig.outputDataName = "guidanceOut"
    attGuidanceConfig.mu = mu
    scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)

    # setup the attitude tracking error evaluation module
    attErrorConfig = attTrackingError.attTrackingErrorConfig()
    attErrorWrap = scSim.setModelDataWrap(attErrorConfig)
    attErrorWrap.ModelTag = "attErrorInertial3D"
    scSim.AddModelToTask(simTaskName, attErrorWrap, attErrorConfig)
    attErrorConfig.outputDataName = "attErrorMsg"
    attErrorConfig.inputRefName = attGuidanceConfig.outputDataName
    attErrorConfig.inputNavName = sNavObject.outputAttName

    # setup the MRP Feedback control module
    mrpControlConfig = MRP_Feedback.MRP_FeedbackConfig()
    mrpControlWrap = scSim.setModelDataWrap(mrpControlConfig)
    mrpControlWrap.ModelTag = "MRP_Feedback"
    scSim.AddModelToTask(simTaskName, mrpControlWrap, mrpControlConfig)
    mrpControlConfig.inputGuidName = attErrorConfig.outputDataName
    mrpControlConfig.vehConfigInMsgName = "vehicleConfigName"
    mrpControlConfig.outputDataName = extFTObject.cmdTorqueInMsgName
    mrpControlConfig.K = 3.5
    mrpControlConfig.Ki = -1.0  # make value negative to turn off integral feedback
    mrpControlConfig.P = 30.0
    mrpControlConfig.integralLimit = 2. / mrpControlConfig.Ki * 0.1
    mrpControlConfig.domega0 = [0.0, 0.0, 0.0]

    # add drag dynamic effector (assumes simple cannonball model, attitude dependency not currently supported)
    dragModelConfig = dragDynamicEffector.DragDynamicEffector()
    dragModelConfig.modelType = "cannonball"
    dragModelConfig.ModelTag = "cannonballDrag"
    dragModelConfig.coreParams.velocityMag = 0.
    dragModelConfig.coreParams.projectedArea = 0.068  # drag area in m^2
    dragModelConfig.coreParams.dragCoeff = 2.0  # coefficient of drag
    dragModelConfig.coreParams.comOffset = [0., 0.05, 0.05]  # distance from center of mass to  center of projected area
    scObject.addDynamicEffector(dragModelConfig)
    scSim.AddModelToTask(simTaskName, dragModelConfig)

    #
    #   Setup data logging before the simulation is initialized
    #
    numDataPoints = 10000
    samplingTime = simulationTime / (numDataPoints - 1)
    scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
    scSim.TotalSim.logThisMessage(sNavObject.outputTransName, samplingTime)
    scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)

    #
    # create simulation messages
    #

    # create the FSW vehicle configuration message
    vehicleConfigOut = fswMessages.VehicleConfigFswMsg()
    vehicleConfigOut.ISCPntB_B = I  # use the same inertia in the FSW algorithm as in the simulation
    unitTestSupport.setMessage(scSim.TotalSim,
                               simProcessName,
                               mrpControlConfig.vehConfigInMsgName,
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

    dataOmegaBR = scSim.pullMessageLogData(sNavObject.outputAttName + ".omega_BN_B", range(3))
    dataPos = scSim.pullMessageLogData(sNavObject.outputTransName + ".r_BN_N", range(3))
    dataVel = scSim.pullMessageLogData(sNavObject.outputTransName + ".v_BN_N", range(3))
    dataSigmaBR = scSim.pullMessageLogData(sNavObject.outputAttName + ".sigma_BN", range(3))
    np.set_printoptions(precision=16)

    #
    #   plot the results
    #
    fileName = os.path.basename(os.path.splitext(__file__)[0])

    timeLineSet = dataSigmaBR[:, 0] * macros.NANO2MIN
    plt.close("all")  # clears out plots from earlier test runs

    figureList = {}
    plot_track_error_norm(timeLineSet, dataSigmaBR)
    pltName = fileName + "1" + str(int(False))
    figureList[pltName] = plt.figure(1)

    #plot_control_torque(timeLineSet, dataLr)
    #pltName = fileName + "2" + str(int(False))
    #figureList[pltName] = plt.figure(2)

    plot_rate_error(timeLineSet, dataOmegaBR)
    pltName = fileName + "3" + str(int(False))
    figureList[pltName] = plt.figure(3)

    plot_orbit(oe, earth.mu, earth.radEquator, dataPos, dataVel)
    pltName = fileName + "4" + str(int(False))
    figureList[pltName] = plt.figure(4)

    if show_plots:
        plt.show()

    return numDataPoints


if __name__ == "__main__":
    run(
        True  # show_plots
        )
