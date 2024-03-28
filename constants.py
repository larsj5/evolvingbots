import numpy

simulation_length = 1000
time_step = 1/30
gravity = -9.8
two_pi = 2 * numpy.pi

# motor values
amplitude = numpy.pi / 6.0
frequency = 10
phaseOffset = numpy.pi / 2.0

BLforce = 20
FLforce = 20

motorJointRange = 0.2

numberOfGenerations = 20
populationSize = 20

numSensorNeurons = 4
numMotorNeurons = 8