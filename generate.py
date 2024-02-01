import pyrosim.pyrosim as pyrosim


def CreateWorld():

    pyrosim.Start_SDF("world.sdf")

    # box sizes
    length = 1
    width = 1
    height = 1

    # box position
    x = 0
    y = 0
    z = 0.5

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

    pyrosim.End()


def CreateRobot():
    pyrosim.Start_URDF("body.urdf")

    # box sizes
    length = 1
    width = 1
    height = 1

    # box position
    x = 0
    y = 0
    z = 0.5

    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])
    pyrosim.End()

CreateWorld()
CreateRobot()