'''My calculator test'''

from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import Operations

def test_add_calculation():
    '''Test adding a calculation to the history'''
    Calculations.clear_history()
    calc = Calculation(Operations.add, [1, 2])
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1

def test_subtract_calculation():
    '''Test subtracting a calculation and adding it to the history'''
    Calculations.clear_history()
    calc = Calculation(Operations.subtract, [5, 3])
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1
    assert Calculations.get_last_calculation().get_result() == 2

def test_multiply_calculation():
    '''Test multiplying a calculation and adding it to the history'''
    Calculations.clear_history()
    calc = Calculation(Operations.multiply, [3, 4])
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1
    assert Calculations.get_last_calculation().get_result() == 12

def test_divide_calculation():
    '''Test dividing a calculation and adding it to the history'''
    Calculations.clear_history()
    calc = Calculation(Operations.divide, [10, 2])
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1
    assert Calculations.get_last_calculation().get_result() == 5

def test_get_last_calculation():
    '''Test retrieving the entire calculation history'''
    calc = Calculation(Operations.multiply, [2, 3])
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation().get_result() == 6

def test_clear_history():
    '''Test clearing the entire calculation history'''
    Calculations.clear_history()
    assert len(Calculations.history) == 0
