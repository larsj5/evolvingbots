from motor import MOTOR
from sensor import SENSOR

import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:

    ### Constructor ###
    def __init__(self):
        # load and prepare to simulate the robot
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Value(t, self.robotId)