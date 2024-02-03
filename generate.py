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


def CreateRobot():
    pyrosim.Start_URDF("body.urdf")

    # Only the first link in a robot --- the "root" link --- has an absolute position.
    # Every other link has a position relative to its "upstream" joint.

    ###### Link 0 #######
    # box sizes
    length = 1
    width = 1
    height = 1

    # box position
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length, width, height])

    # Joints with no upstream joint have absolute positions.
    # Every other joint has a position relative to its upstream joint
    ###### Joint 0_1 ######
    # joint position
    x = 0
    y = 0
    z = 1
    pyrosim.Send_Joint(name = "Link0_Link1", parent= "Link0", child = "Link1", type = "revolute", position = [x,y,z])
                                                                                                              
    ###### Link 1 #######
    # box position -> now is relative
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Link1", pos=[x,y,z] , size=[length, width, height])


    ###### Joint 1_2 ######
    # joint position
    x = 0
    y = 0
    z = 1
    pyrosim.Send_Joint(name = "Link1_Link2", parent= "Link1", child = "Link2", type = "revolute", position = [x,y,z])
                                                                                                              
    ###### Link 2 #######
    # box position -> now is relative
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Link2", pos=[x,y,z] , size=[length, width, height])

    ###### Joint 2_3 ######
    # joint position
    x = 0
    y = 0.5
    z = 0.5
    pyrosim.Send_Joint(name = "Link2_Link3", parent= "Link2", child = "Link3", type = "revolute", position = [x,y,z])
                                                                                                              
    ###### Link 3 #######
    # box position -> now is relative
    x = 0
    y = 0.5
    z = 0

    pyrosim.Send_Cube(name="Link3", pos=[x,y,z] , size=[length, width, height])



    pyrosim.End()

CreateWorld()
CreateRobot()