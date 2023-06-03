from ILogger import ILogger
import logging

class Logger(ILogger):
    def __init__(self, level):
        super().__init__()
        self.logger = logging.getLogger("MyLogger")
        self.file_handler = logging.FileHandler("log.txt")
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def log(self, level):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                #logging
                self.logger.log(level, f'{func.__name__}({args} {kwargs}) returned {result}')
                return result
            return wrapper
        return decorator