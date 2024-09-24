from calculator.operations import Operations
from typing import List

class Calculation:
    def __init__(self, operation, operands: List[float]):
        self.operation = operation
        self.operands = operands
        self.result = self.operation(*self.operands)
    
    def get_result(self) -> float:
        return self.result