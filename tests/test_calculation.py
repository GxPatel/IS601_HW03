'''This module contains tests for calculator operations and calculation class'''

from calculator.calculation import Calculation
from calculator.operations import Operations

def test_create_addition_calculation():
    '''Test calculations for addition.'''
    calc = Calculation(Operations.add, [1, 2])
    assert calc.get_result() == 3

def test_create_subtraction_calculation():
    '''Test calculations for subtraction.'''
    calc = Calculation(Operations.subtract, [5, 3])
    assert calc.get_result() == 2
