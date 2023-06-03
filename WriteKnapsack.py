from IWritableKnapsack import IWritableKnapsack
from IKnapsackProblem import IKnapsackProblem
from ILogger import ILogger
import logging

class WriteKnapsack(IWritableKnapsack):
    def __init__(self, logger: ILogger):
        super().__init__()
        self._logger = logger

    def writeToFile(self, path, knapsack: IKnapsackProblem, saveType: str):
        @self._logger.log(logging.INFO)
        def logableWrite(path, knapsack: IKnapsackProblem, saveType: str):
            with open(path, saveType) as file:
                file.write(str(knapsack.size) + "\n")
                for i in knapsack.items:
                    toWrite = f"{i.value} {i.size}\n"
                    file.write(toWrite)
            return f"Knapsack succesfully saved to file {path}"
        return logableWrite(path, knapsack, saveType)
