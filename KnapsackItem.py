from IKnapsackItem import IKnapsackItem

class KnapsackItem(IKnapsackItem):
    def __init__(self, size, value):
        self._size = size
        self._value = value

    @property
    def size(self):
        return self._size

    @property
    def value(self):
        return self._value
    
    def __str__(self):
        return f"Size: {self.size}; Value: {self.value}"