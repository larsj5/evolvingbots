from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)      
            self.nextAvailableID = self.nextAvailableID + 1  

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
             self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if (self.children[i].fitness < self.parents[i].fitness):
                self.parents[i] = self.children[i]

    def Print(self):
        print()
        for i in self.parents:
            print("Parent Fitness: " + str(self.parents[i].fitness)
                    + " Child Fitness: " + str(self.children[i].fitness))
        print()
        
    def Show_Best(self):
        lowestFitness = 99999
        bestSolution = 0
        for i in self.parents:
            if self.parents[i].fitness < lowestFitness:
                lowestFitness = self.parents[i].fitness
                bestSolution = i

        self.parents[bestSolution].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()