from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:
    ### Constructor ###
    def __init__(self, directOrGUI):
        # setup environment
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # disables debug visualizer
        p.setGravity(0,0,c.gravity)

        # create world and robot
        self.world = WORLD()
        self.robot = ROBOT()

    ### Destructor ###
    def __del__(self):
        p.disconnect()

    ### Run the Simulation ###
    def Run(self):
        for i in range (0, c.simulation_length):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act(i)
            time.sleep(c.time_step)

    def Get_Fitness(self):
        self.robot.Get_Fitness()