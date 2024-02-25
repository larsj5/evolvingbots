import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.simulation_length)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(0, c.two_pi, c.simulation_length) * self.frequency + self.offset)
        
    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, 
                            jointName = self.jointName,
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = self.motorValues[t],
                            maxForce = c.BLforce)