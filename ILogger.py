import abc

class ILogger(abc.ABC):
    def log(self, level):
        pass