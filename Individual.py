from IIndividual import IIndividual
from ISolutionCounter import ISolutionCounter
from IKnapsackProblem import IKnapsackProblem
import random, copy

class Individual(IIndividual):
    def __init__(self, solution: ISolutionCounter, size: int):
        super().__init__()
        self.solution = solution
        self._genotype:list[int] = []
        self._generate(size)
        self._fitness = -1

    #generate a list of genotype
    def _generate(self, size):
        for _ in range(size):
            #random int 0 or 1
            number = random.randint(0, 1)
            self._genotype.append(number)

    @property
    def getGenotype(self):
        return self._genotype
    
    @property
    def fitness(self):
        return self._fitness
    
    @getGenotype.setter
    def setGenotype(self, newGenotype: list[int]):
        self._genotype = newGenotype
        self._fitness = -1

    def countFitness(self, knapsack: IKnapsackProblem):
        newFitness = self.solution.countValue(self._genotype, knapsack)
        #if item count isnt equal to genotype lenght
        if newFitness < 0:
            self._fitness = -2
        #if solution is acceptable
        elif self.solution.isAcceptable(self._genotype, knapsack):
            self._fitness = newFitness
        #if solution isnt acceptable
        else:
            self._fitness = -1

    def __len__(self):
        return len(self._genotype)
    
    def __str__(self):
        return f"{self._genotype}"