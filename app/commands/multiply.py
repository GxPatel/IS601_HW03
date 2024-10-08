from app.commands import Command

class MultiplyCommand(Command):
    def execute(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a * b
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
