from ICrossable import ICrossable
from IIndividual import IIndividual
from ISolutionCounter import ISolutionCounter
from MyExceptions import ExceptionOfSize
import copy

class Crosser(ICrossable):
    def __init__(self, solution: ISolutionCounter):
        super().__init__()
        self.solution = solution

    def cross(self, individual:IIndividual, individual1:IIndividual):
        if len(individual.getGenotype) != len(individual1.getGenotype):
            raise ExceptionOfSize()

        newGenotypes = [[],[]]
        for i in range(len(individual.getGenotype)):
            if i % 2 == 0:
                newGenotypes[0].append(individual.getGenotype[i])
                newGenotypes[1].append(individual1.getGenotype[i])
            else:
                newGenotypes[0].append(individual1.getGenotype[i])
                newGenotypes[1].append(individual.getGenotype[i])
        return copy.deepcopy(newGenotypes[0]), copy.deepcopy(newGenotypes[1])