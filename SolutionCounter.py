from ISolutionCounter import ISolutionCounter
from IKnapsackProblem import IKnapsackProblem

class SolutionCounter(ISolutionCounter):
    def __init__(self):
        super().__init__()

    def countValue(self, genotype:list, knapsack:IKnapsackProblem):
        if len(knapsack.items) != len(genotype):
            return -1
        sum = 0
        for i in range(len(genotype)):
            if genotype[i] == 1:
                sum += knapsack.items[i].value
        return sum

    def countSize(self, genotype:list, knapsack:IKnapsackProblem):
        if len(knapsack.items) != len(genotype):
            return -1
        sum = 0
        for i in range(len(genotype)):
            if genotype[i] == 1:
                sum += knapsack.items[i].size
        return sum

    def isAcceptable(self, genotype:list, knapsack:IKnapsackProblem):
        if len(knapsack.items) != len(genotype):
            return False
        return self.countSize(genotype, knapsack) <= knapsack.size