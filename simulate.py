import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy
import random
import constants as c

# setup environment
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # disables debug visualizer

# setup world 
p.setGravity(0,0,c.GRAVITY)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

# set up sensors
backLegSensorValues = numpy.zeros(c.SIMULATION_LENGTH)
frontLegSensorValues = numpy.zeros(c.SIMULATION_LENGTH)
pyrosim.Prepare_To_Simulate(robotId)

# motors
FLtargetAngles = c.FLamplitude * numpy.sin(numpy.linspace(0, c.TWO_PI, c.SIMULATION_LENGTH) * c.FLfrequency + c.FLphaseOffset)
BLtargetAngles = c.BLamplitude * numpy.sin(numpy.linspace(0, c.TWO_PI, c.SIMULATION_LENGTH) * c.BLfrequency + c.BLphaseOffset)

# numpy.save('data/backLegMotorValues.npy', BLtargetAngles)
# numpy.save('data/frontLegMotorValues.npy', FLtargetAngles)
# exit()

for i in range (0, c.SIMULATION_LENGTH):
    p.stepSimulation()

    #store sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # motors
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_BackLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = BLtargetAngles[i],
                                maxForce = c.BLforce)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_FrontLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = FLtargetAngles[i],
                                maxForce = c.FLforce)
    
    time.sleep(c.TIME_STEP)

# disconnect from environment
p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
