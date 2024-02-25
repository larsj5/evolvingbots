import pyrosim.pyrosim as pyrosim


def CreateWorld():

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


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    # Only the first link in a robot --- the "root" link --- has an absolute position.
    # Every other link has a position relative to its "upstream" joint.

    ###### Link 0 #######
    # box sizes
    length = 1
    width = 1
    height = 1

    # box position
    x = 1.5
    y = 0
    z = 1.5
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])

    # Joints with no upstream joint have absolute positions.
    # Every other joint has a position relative to its upstream joint
    ###### Joint 0_1 ######
    # joint position
    x = 1
    y = 0
    z = 1
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [x,y,z])
                                                                                                              
    ###### Link 1 #######
    # box position -> now is relative
    x = -0.5
    y = 0
    z = -0.5
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length, width, height])

    ###### Joint 1_2 ######
    # joint position
    x = 2
    y = 0
    z = 1
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [x,y,z])
                                                                                                              
    ###### Link 2 #######
    # box position -> now is relative
    x = 0.5
    y = 0
    z = -0.5
    pyrosim.Send_Cube(name="FrontLeg", pos=[x,y,z] , size=[length, width, height])

    pyrosim.End()


def Generate_Brain():

    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
   
    pyrosim.End()

Generate_Body()
Generate_Brain()