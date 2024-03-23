from motor import MOTOR
from sensor import SENSOR
import os

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    ### Constructor ###
    def __init__(self, solutionID):
        # load and prepare to simulate the robot
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("rm brain" + str(solutionID) + ".nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[str.encode(jointName)].Set_Value(desiredAngle, self.robotId)
                # print(f'Neuron Name: {neuronName}, Joint Name: {jointName}, Desired Angle: {desiredAngle}')
            
    def Think(self, t):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        filename = "tmp" + str(self.solutionID) + ".txt"
        f = open(filename, 'w')
        f.write(str(xCoordinateOfLinkZero))
        f.close()

        os.system("mv tmp" + self.solutionID + ".txt fitness" + self.solutionID + ".txt")

        