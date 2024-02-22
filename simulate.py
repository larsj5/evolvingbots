import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()

# # set up sensors
# backLegSensorValues = numpy.zeros(c.simulation_length)
# frontLegSensorValues = numpy.zeros(c.simulation_length)
# pyrosim.Prepare_To_Simulate(robotId)

# # motors
# FLtargetAngles = c.FLamplitude * numpy.sin(numpy.linspace(0, c.two_pi, c.simulation_length) * c.FLfrequency + c.FLphaseOffset)
# BLtargetAngles = c.BLamplitude * numpy.sin(numpy.linspace(0, c.two_pi, c.simulation_length) * c.BLfrequency + c.BLphaseOffset)

# # numpy.save('data/backLegMotorValues.npy', BLtargetAngles)
# # numpy.save('data/frontLegMotorValues.npy', FLtargetAngles)
# # exit()

# for i in range (0, c.simulation_length):
#     p.stepSimulation()

#     #store sensor values
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     # motors
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
#                                 jointName = b'Torso_BackLeg',
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = BLtargetAngles[i],
#                                 maxForce = c.BLforce)
    
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
#                                 jointName = b'Torso_FrontLeg',
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = FLtargetAngles[i],
#                                 maxForce = c.FLforce)
    
#     time.sleep(c.time_step)

# # disconnect from environment
# p.disconnect()

# numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
