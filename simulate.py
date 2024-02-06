import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy

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
pyrosim.Prepare_To_Simulate(robotId)

for i in range (0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/60)

# disconnect from environment
p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
