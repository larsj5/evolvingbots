from motor import MOTOR
from sensor import SENSOR

import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        # load and prepare to simulate the robot
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)