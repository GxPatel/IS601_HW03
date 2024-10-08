from app.commands import Command
import sys

class ExitCommand(Command):
    def execute(self):
        print("Exiting the program...")
        sys.exit(0)
