from calculator.calculation import Calculation
from typing import List

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()