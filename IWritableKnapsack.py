import abc
from IKnapsackProblem import IKnapsackProblem

class IWritableKnapsack(abc.ABC):
    def writeToFile(self, path, knapsack: IKnapsackProblem, saveType: str):
        pass