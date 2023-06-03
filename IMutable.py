import abc
from IIndividual import IIndividual

class IMutable(abc.ABC):
    @abc.abstractmethod
    def mutation(self, mutationProb, individual: IIndividual):
        pass