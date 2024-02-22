from motor import MOTOR
from sensor import SENSOR

import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:

    ### Constructor ###
    def __init__(self):

        self.motors = {}

        # load and prepare to simulate the robot
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)