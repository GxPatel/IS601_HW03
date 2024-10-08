from app.commands import CommandHandler
from app.commands.menu import MenuCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        """Register calculator and general commands"""
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())

        print("Welcome to the interactive calculator!")
        print("Type 'menu' to see available commands or 'exit' to quit.")

        while True:  # REPL: Read-Evaluate-Print Loop
            command_input = input(">>> ").strip()
            self.command_handler.execute_command(command_input)
