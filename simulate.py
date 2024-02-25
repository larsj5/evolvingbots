from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

# # set up sensors
# backLegSensorValues = numpy.zeros(c.simulation_length)
# frontLegSensorValues = numpy.zeros(c.simulation_length)
# pyrosim.Prepare_To_Simulate(robotId)

# # motors
# FLtargetAngles = c.FLamplitude * numpy.sin(numpy.linspace(0, c.two_pi, c.simulation_length) * c.FLfrequency + c.FLphaseOffset)
# BLtargetAngles = c.BLamplitude * numpy.sin(numpy.linspace(0, c.two_pi, c.simulation_length) * c.BLfrequency + c.BLphaseOffset)

# # numpy.save('data/backLegMotorValues.npy', BLtargetAngles)
# # numpy.save('data/frontLegMotorValues.npy', FLtargetAngles)

# for i in range (0, c.simulation_length):
#     p.stepSimulation()

#     #store sensor values
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

# # disconnect from environment
# p.disconnect()

# numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
