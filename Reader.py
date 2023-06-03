from IReader import IReader
from ILogger import ILogger
import os, logging

class Reader(IReader):
    def __init__(self, logger: ILogger):
        super().__init__()
        self._logger = logger

    def read(self, path):
        @self._logger.log(logging.INFO)
        def readToLog(path):
            if os.path.isfile(path):
                #open file
                returnList = []
                with open(path, 'r') as file:
                    for line in file:
                        returnList.append(line.split())
                return returnList
            else:
                return None
        return readToLog(path)
