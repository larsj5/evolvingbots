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

        # box sizes
        length = 1
        width = 1
        height = 1

        # box position
        x = 4
        y = 4
        z = 0.5

        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

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
        # box sizes and positions
        length = 1
        width = 1
        height = 1

        x = 0
        y = 0
        z = 1

        pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])
        # ------------ END TORSO --------------# 


        # ------------- BACK LEG ----------------# 
        # joint position
        x = 0
        y = -0.5
        z = 1

        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [x,y,z], jointAxis="1 0 0")

        # update link sizes
        length = 0.2
        width = 1
        height = 0.2

        # box position [relative]
        x = 0
        y = -0.5
        z = 0

        pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length, width, height])
        # ------------- END BACK LEG ----------------# 

        
        # ------------- FRONT LEG ----------------# 
        # joint position
        x = 0
        y = 0.5
        z = 1
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [x,y,z], jointAxis="1 0 0")
                                                                                                                
        # box position [relative]
        x = 0
        y = 0.5
        z = 0

        pyrosim.Send_Cube(name="FrontLeg", pos=[x,y,z] , size=[length, width, height])
        # ------------- END FRONT LEG ----------------# 


        # ------------- LEFT LEG ----------------# 
        # joint position
        x = -0.5
        y = 0
        z = 1

        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent= "Torso", child = "LeftLeg", type = "revolute", position = [x,y,z], jointAxis="0 1 0")

        # update link sizes
        length = 1
        width = 0.2
        height = 0.2

        # box position [relative]
        x = -0.5
        y = 0
        z = 0

        pyrosim.Send_Cube(name="LeftLeg", pos=[x,y,z] , size=[length, width, height])
        # ------------- END LEFT LEG ----------------# 


        # ------------- RIGHT LEG ----------------# 
        # joint position
        x = 0.5
        y = 0
        z = 1

        pyrosim.Send_Joint(name = "Torso_RightLeg", parent= "Torso", child = "RightLeg", type = "revolute", position = [x,y,z], jointAxis="0 1 0")

        # box position [relative]
        x = 0.5
        y = 0
        z = 0

        pyrosim.Send_Cube(name="RightLeg", pos=[x,y,z] , size=[length, width, height])
        # ------------- END RIGHT LEG ----------------# 
        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")


        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 0 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 1 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 2 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + 3 , jointName = "Torso_RightLeg")

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
