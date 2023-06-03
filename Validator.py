from IValidator import IValidator
from ILogger import ILogger
import logging

class Validator(IValidator):
    def __init__(self, logger: ILogger):
        super().__init__()
        self._logger = logger

    def validate(self, readedFile):
        @self._logger.log(logging.INFO)
        def validateLogable(readedFile):
            if len(readedFile) <= 2:
                return False
            #size must be min 1 and size must be 1
            if len(readedFile[0]) != 1 or int(readedFile[0][0]) < 1:
                return False
            #check values for each list from readed file
            for i in range(1, len(readedFile)):
                #each list for item has to has 2 values (size and value)
                if len(readedFile[i]) != 2:
                    return False
                #each size an value has to be min 1
                for number in readedFile[i]:
                    if int(number) <= 0:
                        return False
            return True
        return validateLogable(readedFile)
