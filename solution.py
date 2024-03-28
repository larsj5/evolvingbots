import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = (self.weights * 2) - 1
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        # setup
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # run
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        filename = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(filename):
            time.sleep(0.01)
        f = open(filename, 'r')
        self.fitness = float(f.readline())
        f.close()
        os.system("rm " + filename)

    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[1,1,1] , size=[4, 4, 0.5])

        pyrosim.End()


    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        # ------------- Comments ----------------# 
        # Only the first link in a robot --- the "root" link --- has an absolute position.
        # Every other link has a position relative to its "upstream" joint.
        # Joints with no upstream joint have absolute positions.
        # Every other joint has a position relative to its upstream joint
        # ---------------------------------------# 

        # ------------- TORSO ----------------# 
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1, 1, 1])
        # ------------ END TORSO --------------# 


        # ------------- BACK LEG ----------------# 
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [0,-0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2, 1, 0.2])

        # joint position is relative to back leg        
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent= "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0,-1,0], jointAxis="1 0 0")                                                                                             
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2, 0.2, 1])
        # ------------- END BACK LEG ----------------# 

        
        # ------------- FRONT LEG ----------------# 
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [0,0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2, 1, 0.2])

        # joint position [relative to front leg]
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent= "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [1,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2, 0.2, 1])
        # ------------- END FRONT LEG ----------------# 


        # ------------- LEFT LEG ----------------# 
        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent= "Torso", child = "LeftLeg", type = "revolute", position = [-0.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1, 0.2, 0.2])
        # ------------- END LEFT LEG ----------------# 


        # ------------- RIGHT LEG ----------------# 
        pyrosim.Send_Joint(name = "Torso_RightLeg", parent= "Torso", child = "RightLeg", type = "revolute", position = [0.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1, 0.2, 0.2])
        # ------------- END RIGHT LEG ----------------# 

        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # --------------- Sensor Neurons ------------------#
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")

        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")


        # --------------- Motor Neurons ------------------#
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 0 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 1 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 2 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 3 , jointName = "Torso_RightLeg")

        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 4 , jointName = "FrontLeg_FrontLowerLeg")





        # iterate over the sensor neurons
        for currentRow in range (c.numSensorNeurons):
            # iterate over the motor neurons
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )


        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row][col] = (random.random() * 2) - 1
    
    def Set_ID(self, ID):
        self.myID = ID
