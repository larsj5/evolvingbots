import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy
import random

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
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)

for i in range (0, 1000):
    p.stepSimulation()

    #store sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # motors
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_BackLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = (random.random() % (numpy.pi / 2.0)),
                                maxForce = 25)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = b'Torso_FrontLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = (random.random() % (numpy.pi / 2.0)),
                                maxForce = 25)
    
    time.sleep(1/60)

# disconnect from environment
p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
