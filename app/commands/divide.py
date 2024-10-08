from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = a / b
                print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
