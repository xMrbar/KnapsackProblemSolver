import abc

class IValidator(abc.ABC):
    def validate(self, readedFile):
        pass