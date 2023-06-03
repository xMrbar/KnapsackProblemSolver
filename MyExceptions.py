class ExceptionOfSize(Exception):
    def __init__(self, message="Size problem. Check parametrs"):
        super().__init__(self.message)
        self.message = message

class ExceptionOfValue(Exception):
    def __init__(self, message="Value cant be less or equal 0"):
        super().__init__(self.message)
        self.message = message