from IKnapsackProblem import IKnapsackProblem
from IKnapsackItem import IKnapsackItem

class KnapsackProblem(IKnapsackProblem):
    def __init__(self, size):
        super().__init__()
        self._size = size
        self._items = []

    def addItem(self, item: IKnapsackItem):
        self._items.append(item)

    def deleteItem(self, itemIndex):
        self._items.pop(itemIndex)
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def setSize(self, newSize):
        self._size = newSize
    
    @property
    def items(self):
        return self._items

    def getKnapsackValues(self):
        allValues = []
        for i in self._items:
            allValues.append(i.value)
        return allValues

    def getKnapsackSizes(self):
        allSizes = []
        for i in self._items:
            allSizes.append(i.size)
        return allSizes
    
    def __str__(self):
        return f"{self.items}"