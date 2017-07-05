class BitwiseOperationError(RuntimeError):
    def __init__(self,message):
        self.message = message