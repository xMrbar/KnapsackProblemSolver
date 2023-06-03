from IWritableSolution import IWritableSolution
from IKnapsackProblem import IKnapsackProblem
from ILogger import ILogger
import logging

class WriteSolution(IWritableSolution):
    def __init__(self, logger: ILogger):
        super().__init__()
        self._logger = logger

    def writeToFile(self, path, strSolution, saveType: str):
        @self._logger.log(logging.INFO)
        def logableWrite(path, strSolution, saveType: str):
            with open(path, saveType) as file:
                file.write(strSolution)
                file.write("\n")
            return f"Solution succesfully saved to file {path}"
        return logableWrite(path, strSolution, saveType)

        