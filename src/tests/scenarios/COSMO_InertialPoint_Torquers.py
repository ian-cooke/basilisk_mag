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
# Purpose:  Integrated test of the spacecraftPlus(), extForceTorque, simpleNav(),
#           MRP_Feedback() with attitude navigation modules.  This script is a
#           spinoff from the attitude guidance tutorial, it implements a hyperbolic
#           trajectory and uses the velocityPoint module.
# Author:   Anne Bennett
# Creation Date:  Aug. 28th, 2017
#

import inspect
import os
import numpy as np
from datetime import datetime
from Basilisk import __path__

import matplotlib.pyplot as plt
from Basilisk.fswAlgorithms import MRP_Feedback, attTrackingError, fswMessages, velocityPoint, mag_attTrack, \
    inertial3D
from Basilisk.simulation import extForceTorque, simple_nav, spacecraftPlus, simMessages, eclipse, \
    mag_meter, torqueRodDynamicEffector
from Basilisk.utilities import SimulationBaseClass, macros, orbitalMotion, simIncludeGravBody
# general support file with common unit test functions
from Basilisk.utilities import unitTestSupport

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
    p1ds = plt.axhline(y=1, color='r', linestyle='--', label='+1 deg/s')
    n1ds = plt.axhline(y=-1, color='r', linestyle='--', label='-1 deg/s')
    plt.legend(loc='lower right')
    plt.xlabel('Time [min]')
    plt.ylabel('Rate Tracking Error [deg/s] ')


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
    fData = np.linspace(0, 2 * np.pi, 100)
    rData = []
    for idx in range(0, len(fData)):
        rData.append(p / (1 + oe.e * np.cos(fData[idx])))
    plt.plot(rData * np.cos(fData) / 1000, rData * np.sin(fData) / 1000, '--', color='#555555', label='Orbit Track')
    plt.xlabel('$i_e$ Cord. [km]')
    plt.ylabel('$i_p$ Cord. [km]')
    plt.legend(loc='lower left')
    plt.grid()

## \defgroup Tutorials_2_1_1
## @{
# How to use guidance modules to align the spacecraft frame to the velocity-pointing frame.
#
# Attitude Alignment for a Spacecraft on a Hyperbolic Trajectory {#scenarioAttGuideHyperbolic}
# ====
#
# Scenario Description
# -----
# This script sets up a 6-DOF spacecraft which is on a hyperbolic trajectory near Earth.
# It aligns the spacecraft to point along the velocity vector throughout the orbit.
#  The scenario is setup to be run in two different configurations:
# Setup | useAltBodyFrame
# ----- | -------------------
# 1     | False
# 2     | True
#
# To run the default scenario 1., call the python script through
#
#       python scenarioAttGuideHyperbolic.py
#
# The simulation layout is shown in the following illustration.  A single simulation process is created
# which contains both the spacecraft simulation modules, as well as the Flight Software (FSW) algorithm
# modules.
# ![Simulation Flow Diagram](Images/doc/test_scenarioAttGuideHyperbolic.svg "Illustration")
#
# When the simulation completes 4 plots are shown. This first three show the MRP attitude history, the rate
# tracking errors, and the control torque vector. The fourth shows the hyperbolic trajectory
# and the segment of that trajectory flown during the simulation.
#
# The basic simulation setup is the same as the one used in
# [scenarioAttitudeGuidance.py](@ref scenarioAttitudeGuidance).
# The dynamics simulation is setup using a SpacecraftPlus() module to which a gravity
# effector is attached.  Note that both the rotational and translational degrees of
# freedom of the spacecraft hub are turned on here to get a 6-DOF simulation.  For more
# information on how to setup an orbit, see [scenarioBasicOrbit.py](@ref scenarioBasicOrbit)
#
# Where the Attitude Guidance Tutorial pointed the spacecraft relative to the Hill frame, this tutorial
# points it relative to the velocity vector.
# Note that mu must be assigned to attGuidanceConfig.mu when using the velocityPoint() module:
# ~~~~~~~~~~~~~{.py}
#     attGuidanceConfig = velocityPoint.velocityPointConfig()
#     attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
#     attGuidanceWrap.ModelTag = "velocityPoint"
#     attGuidanceConfig.inputNavDataName = sNavObject.outputTransName
#     attGuidanceConfig.inputCelMessName = earth.bodyInMsgName
#     attGuidanceConfig.outputDataName = "guidanceOut"
#     attGuidanceConfig.mu = mu
#     scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)
# ~~~~~~~~~~~~~
# Note that in contrast to Hill pointing mode used in
# [scenarioAttitudeGuidance.py](@ref scenarioAttitudeGuidance), the orbit velocity frame pointing
# requires the attacting celestial body gravitational constant mu to be set.
#
# Setup 1
# -----
#
# Which scenario is run is controlled at the bottom of the file in the code
# ~~~~~~~~~~~~~{.py}
# if __name__ == "__main__":
#     run(
#          True,        # show_plots
#          False        # useAltBodyFrame
#        )
# ~~~~~~~~~~~~~
# The first 2 arguments can be left as is.  The remaining argument controls the
# simulation scenario flags to turn on or off certain simulation conditions.  The
# default scenario shown has the `useAltBodyFrame` flag turned off.  This means that we seek
# to align the body frame *B* with the velocity vector *V*.
# ![MRP Attitude History](Images/Scenarios/scenarioAttGuideHyperbolic10.svg "MRP history")
# ![Control Torque History](Images/Scenarios/scenarioAttGuideHyperbolic20.svg "Torque history")
# ![Rate Tracking Error](Images/Scenarios/scenarioAttGuideHyperbolic30.svg "Rate Tracking Error")
# ![Hyperbolic Orbit Illustration](Images/Scenarios/scenarioAttGuideHyperbolic40.svg "Hyperbolic Orbit Illustration")
#
#
# Setup 2
# -----
#
# To run the second scenario, change the main routine at the bottom of the file to read:
# ~~~~~~~~~~~~~{.py}
# if __name__ == "__main__":
#     run(
#          True,        # show_plots
#          True         # useAltBodyFrame
#        )
# ~~~~~~~~~~~~~
# Here the control should not align the principal body frame *B* with *V*, but rather an alternate,
# corrected body frame *Bc*.  For example, if a thruster is located on the \f$\hat b_1\f$ face, and it
# is desired to point it along the negative V-bar, this is achieved through:
# ~~~~~~~~~~~~~{.py}
#   attErrorConfig.sigma_R0R = [0,0,-1]
# ~~~~~~~~~~~~~
# This corrected body frame has an orientation which is rotated 180 degrees about \f$\hat b_3\f$,
# to point the correct face of the spacecraft along the negative V-bar.
#
# The resulting attitude and control torque histories are shown below.
# ![MRP Attitude History](Images/Scenarios/scenarioAttGuideHyperbolic11.svg "MRP history")
# ![Control Torque History](Images/Scenarios/scenarioAttGuideHyperbolic21.svg "Torque history")
# ![Rate Tracking Error](Images/Scenarios/scenarioAttGuideHyperbolic31.svg "Rate Tracking Error")
#
## @}
def run(show_plots, useAltBodyFrame):
    '''Call this routine directly to run the tutorial scenario.'''

    # Create simulation variable names
    simTaskName = "simTask"
    simProcessName = "simProcess"

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()
    scSim.TotalSim.terminateSimulation()

    # set the simulation time variable used later on
    simulationTime = macros.min2nano(180.0)

    #
    #  create the simulation process
    #
    dynProcess = scSim.CreateNewProcess(simProcessName)

    # create the dynamics task and specify the integration update time
    simulationTimeStep = macros.sec2nano(0.05)
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
    #   initialize Spacecraft States with initialization variables
    #
    # setup the orbit using classical orbit elements
    oe = orbitalMotion.ClassicElements()
    orbitRadius = 415.28
    oe.a = (6371.0 + orbitRadius) * 1000.0  # meters
    oe.e = 0.0003449
    oe.i = 51.6388 * macros.D2R
    oe.Omega = 0.0 * macros.D2R
    oe.omega = 0.0 * macros.D2R
    oe.f = 180.0 * macros.D2R
    rN, vN = orbitalMotion.elem2rv(mu, oe)
    scObject.hub.r_CN_NInit = unitTestSupport.np2EigenVectorXd(rN)  # m   - r_CN_N
    scObject.hub.v_CN_NInit = unitTestSupport.np2EigenVectorXd(vN)  # m/s - v_CN_N
    scObject.hub.sigma_BNInit = [[0.4], [0.2], [-0.3]]  # sigma_BN_B
    scObject.hub.omega_BN_BInit = [[5.5 * macros.D2R], [5.5 * macros.D2R], [-5.5 * macros.D2R]]  # rad/s - omega_CN_B
    #scObject.hub.omega_BN_BInit = [[1.0 * macros.D2R], [1.0 * macros.D2R], [-1.0 * macros.D2R]]  # rad/s - omega_CN_B

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

    #
    #   setup the FSW algorithm tasks
    #

    # set up inertial3D guidance module
    attGuidanceConfig = inertial3D.inertial3DConfig()
    attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
    attGuidanceWrap.ModelTag = "inertial3D"
    attGuidanceConfig.sigma_R0N = [0., 0., 0.]
    attGuidanceConfig.outputDataName = "guidanceInertial3D"
    scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)

    # setup velocityPoint guidance module
    #attGuidanceConfig = velocityPoint.velocityPointConfig()
    #attGuidanceWrap = scSim.setModelDataWrap(attGuidanceConfig)
    #attGuidanceWrap.ModelTag = "velocityPoint"
    #attGuidanceConfig.inputNavDataName = sNavObject.outputTransName
    #attGuidanceConfig.inputCelMessName = earth.bodyInMsgName
    #attGuidanceConfig.outputDataName = "guidanceOut"
    #attGuidanceConfig.mu = mu
    #scSim.AddModelToTask(simTaskName, attGuidanceWrap, attGuidanceConfig)

    # setup the attitude tracking error evaluation module
    attErrorConfig = attTrackingError.attTrackingErrorConfig()
    attErrorWrap = scSim.setModelDataWrap(attErrorConfig)
    attErrorWrap.ModelTag = "attErrorInertial3D"
    scSim.AddModelToTask(simTaskName, attErrorWrap, attErrorConfig)
    attErrorConfig.outputDataName = "attErrorInertial3DMsg"
    if useAltBodyFrame:
        attErrorConfig.sigma_R0R = [0, 0, -1]
    attErrorConfig.inputRefName = attGuidanceConfig.outputDataName
    attErrorConfig.inputNavName = sNavObject.outputAttName

    # setup the MRP Feedback control module
    #mrpControlConfig = MRP_Feedback.MRP_FeedbackConfig()
    #mrpControlWrap = scSim.setModelDataWrap(mrpControlConfig)
    #mrpControlWrap.ModelTag = "MRP_Feedback"
    #scSim.AddModelToTask(simTaskName, mrpControlWrap, mrpControlConfig)
    #mrpControlConfig.inputGuidName = attErrorConfig.outputDataName
    #mrpControlConfig.vehConfigInMsgName = "vehicleConfigName"
    #mrpControlConfig.outputDataName = extFTObject.cmdTorqueInMsgName
    #mrpControlConfig.K = 0.005
    #mrpControlConfig.Ki = 0.1  # make value negative to turn off integral feedback
    #mrpControlConfig.P = 0.005
    #mrpControlConfig.integralLimit = 2. / mrpControlConfig.Ki * 0.1
    #mrpControlConfig.domega0 = [0.0, 0.0, 0.0]

    # Add Mag Meter
    MagMeter = mag_meter.MagMeter()
    MagMeter.ModelTag = "MagMeter"
    MagMeterNoise = 0.00000
    MagMeterBias = 0.0
    MagMeter.PMatrix = np.eye(3) * MagMeterNoise
    MagMeter.inclination = oe.i
    MagMeter.orbitRadius = oe.a / 1000  # 6371.0 + orbitRadius
    scSim.AddModelToTask(simTaskName, MagMeter)

    # setup the mag_attTrack Feedback control module
    mag_attTrackControlConfig = mag_attTrack.mag_attTrackConfig()
    mag_attTrackControlWrap = scSim.setModelDataWrap(mag_attTrackControlConfig)
    mag_attTrackControlWrap.ModelTag = "mag_attTrack"
    scSim.AddModelToTask(simTaskName, mag_attTrackControlWrap, mag_attTrackControlConfig)
    mag_attTrackControlConfig.inputGuidName = attErrorConfig.outputDataName
    mag_attTrackControlConfig.inputMagMeterName = MagMeter.outputStateMessage
    mag_attTrackControlConfig.vehConfigInMsgName = "vehicleConfigName"
    mag_attTrackControlConfig.outputDataName = "LrRequested"
    mag_attTrackControlConfig.K_sigma = 10
    mag_attTrackControlConfig.K_omega = 10
    mag_attTrackControlConfig.controlLaw = 2
    mag_attTrackControlConfig.use_rw_wheels = 0

    # setup torque rods
    torqueRodConfig = torqueRodDynamicEffector.torqueRodDynamicEffector()
    # torqueRodWrap = scSim.setModelDataWrap(torqueRodConfig)
    torqueRodConfig.ModelTag = "torqueRods"
    torqueRodConfig.magFieldMsgName = MagMeter.outputStateMessage
    torqueRodConfig.cmdTorqueRodsMsgName = mag_attTrackControlConfig.outputDataName
    torqueRodConfig.torqueRodOutputMsgName = "torqueRodOutput"
    torqueRodConfig.MaxDipoleMoment = 0.11  # [Am^2]
    scObject.addDynamicEffector(torqueRodConfig)
    scSim.AddModelToTask(simTaskName, torqueRodConfig)

    #
    #   Setup data logging before the simulation is initialized
    #
    numDataPoints = 10000
    samplingTime = simulationTime / (numDataPoints - 1)
    scSim.TotalSim.logThisMessage(mag_attTrackControlConfig.outputDataName, samplingTime)
    scSim.TotalSim.logThisMessage(attErrorConfig.outputDataName, samplingTime)
    scSim.TotalSim.logThisMessage(sNavObject.outputTransName, samplingTime)
    scSim.TotalSim.logThisMessage(sNavObject.outputAttName, samplingTime)
    scSim.TotalSim.logThisMessage(torqueRodConfig.torqueRodOutputMsgName)

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
    dataLr = scSim.pullMessageLogData(torqueRodConfig.torqueRodOutputMsgName + ".torque_constrained", range(3))
    dataDipole = scSim.pullMessageLogData(torqueRodConfig.torqueRodOutputMsgName + ".dipole_constrained", range(3))
    dataSigmaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".sigma_BR", range(3))
    dataOmegaBR = scSim.pullMessageLogData(attErrorConfig.outputDataName + ".omega_BR_B", range(3))
    dataPos = scSim.pullMessageLogData(sNavObject.outputTransName + ".r_BN_N", range(3))
    dataVel = scSim.pullMessageLogData(sNavObject.outputTransName + ".v_BN_N", range(3))
    dataSigmaBN = scSim.pullMessageLogData(sNavObject.outputAttName + ".sigma_BN", range(3))
    np.set_printoptions(precision=16)

    #
    #   plot the results
    #
    fileName = os.path.basename(os.path.splitext(__file__)[0])

    timeLineSet = dataSigmaBR[:, 0] * macros.NANO2MIN
    plt.close("all")  # clears out plots from earlier test runs

    figureList = {}
    plot_track_error_norm(timeLineSet, dataSigmaBR)
    pltName = fileName + "1" + str(int(useAltBodyFrame))
    figureList[pltName] = plt.figure(1)

    #plot_control_torque(timeLineSet, dataLr)
    #pltName = fileName + "2" + str(int(useAltBodyFrame))
    #figureList[pltName] = plt.figure(2)

    plot_rate_error(timeLineSet, dataOmegaBR)
    pltName = fileName + "3" + str(int(useAltBodyFrame))
    figureList[pltName] = plt.figure(3)

    plot_orbit(oe, earth.mu, earth.radEquator, dataPos, dataVel)
    pltName = fileName + "4" + str(int(useAltBodyFrame))
    figureList[pltName] = plt.figure(4)

    if show_plots:
        plt.show()

    # close the plots to avoid over-writing old and new figures
    plt.close("all")

    return dataPos, dataSigmaBN, numDataPoints, figureList


#
# This statement below ensures that the unit test scrip can be run as a
# stand-along python script
#
if __name__ == "__main__":
    run(
        True,  # show_plots
        False  # useAltBodyFrame
        )
