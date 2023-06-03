import abc
from IKnapsackItem import IKnapsackItem

class IKnapsackProblem(abc.ABC):
    @abc.abstractproperty
    def size(self):
        pass

    @size.setter
    @abc.abstractmethod
    def setSize(self, newSize):
        pass

    @abc.abstractproperty
    def items(self) -> list[IKnapsackItem]:
        pass

    @abc.abstractmethod
    def getKnapsackValues(self):
        pass

    @abc.abstractmethod
    def getKnapsackSizes(self):
        pass

    @abc.abstractmethod
    def addItem(self, item: IKnapsackItem):
        pass

    @abc.abstractmethod
    def deleteItem(self, itemIndex):
        pass