import abc
from IKnapsackProblem import IKnapsackProblem

class ISolutionCounter(abc.ABC):
    @abc.abstractmethod
    def countValue(self, genotype:list, knapsack:IKnapsackProblem):
        pass

    @abc.abstractmethod
    def countSize(self, genotype:list, knapsack:IKnapsackProblem):
        pass

    @abc.abstractmethod
    def isAcceptable(self, genotype:list, knapsack:IKnapsackProblem):
        pass