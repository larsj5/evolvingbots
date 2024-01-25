import pybullet as p
import time
import pybullet_data

# setup environment
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # disables debug visualizer

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")

for i in range (0, 1000):
    p.stepSimulation()
    time.sleep(1/60)

# disconnect from environment
p.disconnect()