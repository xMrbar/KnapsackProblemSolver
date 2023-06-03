import abc
from IIndividual import IIndividual

class ICrossable(abc.ABC):
    @abc.abstractmethod
    def cross(self, individual:IIndividual, individual1:IIndividual):
        pass
