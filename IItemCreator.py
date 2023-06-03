import abc
from IKnapsackItem import IKnapsackItem

class IItemCreator(abc.ABC):
    @abc.abstractmethod
    def createItem(self, value, size) -> IKnapsackItem:
        pass