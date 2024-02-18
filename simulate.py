import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy
import random

SIMULATION_LENGTH = 1000
# setup environment
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # disables debug visualizer

# setup world 
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

# set up sensors
backLegSensorValues = numpy.zeros(SIMULATION_LENGTH)
frontLegSensorValues = numpy.zeros(SIMULATION_LENGTH)
pyrosim.Prepare_To_Simulate(robotId)

# motor values
FLamplitude = numpy.pi / 6.0
FLfrequency = 10
FLphaseOffset = numpy.pi / 2.0

FLtargetAngles = FLamplitude * numpy.sin(numpy.linspace(0, 2 * numpy.pi, SIMULATION_LENGTH) * FLfrequency + FLphaseOffset)

BLamplitude = 0
BLfrequency = 0
BLphaseOffset = 0

BLtargetAngles = BLamplitude * numpy.sin(numpy.linspace(0, 2 * numpy.pi, SIMULATION_LENGTH) * BLfrequency + BLphaseOffset)

# numpy.save('data/backLegMotorValues.npy', BLtargetAngles)
# numpy.save('data/frontLegMotorValues.npy', FLtargetAngles)
# exit()

for i in range (0, SIMULATION_LENGTH):
    p.stepSimulation()

    #store sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # motors
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_BackLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = BLtargetAngles[i],
                                maxForce = 20)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_FrontLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = FLtargetAngles[i],
                                maxForce = 20)
    
    time.sleep(1/60)

# disconnect from environment
p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
