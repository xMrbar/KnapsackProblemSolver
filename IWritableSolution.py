import abc
from IKnapsackProblem import IKnapsackProblem

class IWritableSolution(abc.ABC):
    def writeToFile(self, path, strSolution, saveType: str):
        pass