import sys
from decimal import Decimal, InvalidOperation
from calculator.operations import Operations

class OperationCommand:
    """Class to execute an operation command."""
    def __init__(self, operation_name, a: Decimal, b: Decimal):
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        # Retrieve the operation method from the Operations class using getattr
        operation_method = getattr(Operations, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a: str, b: str, operation_name: str):
    """Converts inputs to decimal and executes the operation."""
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to handle command-line arguments and trigger calculations."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
