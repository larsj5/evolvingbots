import numpy
import matplotlib.pyplot as plt

targetAngles = numpy.load("data/targetAngles.npy")
# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

backLegMotorValues = numpy.load("data/backLegMotorValues.npy")
frontLegMotorValues = numpy.load("data/frontLegMotorValues.npy")

plt.plot(targetAngles)
# plt.plot(backLegSensorValues, label='Back Leg', linewidth=2)
# plt.plot(frontLegSensorValues, label='Front Leg')

plt.plot(backLegMotorValues, label='Back Leg', linewidth=2)
plt.plot(frontLegMotorValues, label='Front Leg')

plt.legend()
plt.show()
