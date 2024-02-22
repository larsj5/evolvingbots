from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        
        # setup environment
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # disables debug visualizer
        p.setGravity(0,0,c.gravity)

        # create world and robot
        self.world = WORLD()
        self.robot = ROBOT()