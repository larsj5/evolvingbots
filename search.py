import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

os.system("rm brain*.nndf")
os.system("rm fitness*.txt")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()