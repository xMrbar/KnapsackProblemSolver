from IKnapsackItem import IKnapsackItem
from IItemCreator import IItemCreator
from KnapsackItem import KnapsackItem

class ItemCreator(IItemCreator):
    def createItem(self, value, size) -> IKnapsackItem:
        return KnapsackItem(size, value)