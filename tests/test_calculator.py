'''Calculator Operations Tests'''
from calculator.operations import Operations

def test_addition():
    '''Test that addition function works'''
    assert Operations.add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert Operations.subtract(2, 2) == 0

def test_divide():
    '''Test that division function works'''
    assert Operations.divide(2, 2) == 1

def test_divide_by_zero():
    '''Test that division by zero raises an exception'''
    try:
        Operations.divide(2, 0)
        assert False  # Fail if no exception is raised
    except ZeroDivisionError:
        assert True  # Pass if ZeroDivisionError is raised

def test_multiply():
    '''Test that multiplication function works'''
    assert Operations.multiply(2, 2) == 4
