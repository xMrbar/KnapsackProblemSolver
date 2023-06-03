import abc

class IReader(abc.ABC):
    def read(self, path):
        pass