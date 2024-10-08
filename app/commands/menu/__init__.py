from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print("Available commands:")
        print(" - add: Add two numbers")
        print(" - subtract: Subtract two numbers")
        print(" - multiply: Multiply two numbers")
        print(" - divide: Divide two numbers")
        print(" - menu: Display this menu")
        print(" - exit: Exit the program")
