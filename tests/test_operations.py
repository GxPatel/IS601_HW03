'''Testing operations'''

import pytest
from calculator.operations import Operations

def test_add():
    '''Testing the addition operation'''
    assert Operations.add(1, 2) == 3

def test_subtract():
    '''Testing the subtraction operation'''
    assert Operations.subtract(5, 3) == 2

def test_multiply():
    '''Testing the multiplication operation'''
    assert Operations.multiply(2, 3) == 6

def test_divide():
    '''Testing the division operation'''
    assert Operations.divide(10, 2) == 5

def test_divide_by_zero():
    '''Testing the division by 0 exception'''
    with pytest.raises(ZeroDivisionError):
        Operations.divide(10, 0)
