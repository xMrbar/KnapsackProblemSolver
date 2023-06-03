import abc

class IKnapsackItem(abc.ABC):
    @abc.abstractproperty
    def size(self):
        pass

    @abc.abstractproperty
    def value(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass