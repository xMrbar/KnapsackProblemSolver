import abc
from IKnapsackProblem import IKnapsackProblem

class IIndividual(abc.ABC):
    @abc.abstractmethod
    def countFitness(self, knapsack: IKnapsackProblem):
        pass

    @abc.abstractproperty
    def getGenotype(self):
        pass

    @abc.abstractproperty
    def fitness(self):
        pass

    @getGenotype.setter
    @abc.abstractmethod
    def setGenotype(self, newGenotype: list[int]):
        pass
