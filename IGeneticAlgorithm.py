import abc
from IIndividual import IIndividual

class IGeneticAlgorithm(abc.ABC):
    @abc.abstractmethod
    def runAlgorithm(self, numberOfIteration: int, numerOfIndividuals: int, 
                     crossProb: float, mutationProb: float) -> IIndividual | None | int:
        pass