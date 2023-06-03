import abc
from IIndividual import IIndividual

class IIndividualCreator(abc.ABC):
    @abc.abstractmethod
    def createItem(self, solution, size) -> IIndividual:
        pass