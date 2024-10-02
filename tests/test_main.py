'''Test cases for the main.py module'''
import pytest
from main import calculate_and_print

# Parameterized tests to cover different operations and scenarios
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "Error: Division by zero."),  # Division by zero case
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Invalid input test
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Another invalid input test
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_print function for various inputs."""
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()  # Capture printed output
    assert captured.out.strip() == expected_string
