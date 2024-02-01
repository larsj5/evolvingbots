import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("world.sdf")

# box sizes
length = 1
width = 1
height = 1

# box position
x = 0
y = 0
z = 0.5

# shrinking variable
shrink = .9

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])


# x direction
# for j in range(5):

#     # y direction
#     for k in range (5):

#         # create one tower
#         for i in range (10):
#             pyrosim.Send_Cube(name="Box" + str(i), pos=[x + k,y + j,z + i] , size=[length, width, height])

#             #update sizes
#             length = length * shrink
#             width = width * shrink
#             height = height * shrink
        
#         # reset sizes
#         length = 1
#         width = 1
#         height = 1

pyrosim.End()