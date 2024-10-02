'''conftest.py'''
from decimal import Decimal
from faker import Faker
from calculator.operations import Operations

fake = Faker()
'''Pytest configuration file for generating test data using Faker'''
def generate_test_data(num_records):
    """Generate random test data for various operations"""
    operation_mappings = {
        'add': Operations.add,
        'subtract': Operations.subtract,
        'multiply': Operations.multiply,
        'divide': Operations.divide
    }
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        if operation_func is Operations.divide:
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func is Operations.divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''Add a command line option to control the number of test records'''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate test cases dynamically based on the test function's needs"""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
