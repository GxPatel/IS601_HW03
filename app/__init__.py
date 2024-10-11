import os
import sys
import pkgutil
import importlib
import logging
import logging.config
from app.commands import Command
from app.commands import CommandHandler
from app.commands.menu import MenuCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from dotenv import load_dotenv

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)  # create logs directory
        self.configure_logging() 
        load_dotenv()  # load env vars. from .env file
        self.settings = self.load_environment_variables()  
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler() 

    def configure_logging(self):
        """Set up logging configuration."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables into the settings."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        """Dynamically load plugins from the app.plugins package."""
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Register commands from the plugin modules."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        """Start the application and enter the REPL loop."""
        self.load_plugins()  # Load external plugins (if any)
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())

        logging.info("Application started. Type 'exit' to quit.")
        print("Welcome to the interactive calculator!")
        print("Type 'menu' to see available commands or 'exit' to quit.")
        
        try:
            while True:  # REPL loop
                command_input = input(">>> ").strip()
                if command_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)
                try:
                    self.command_handler.execute_command(command_input)
                except KeyError:
                    logging.error(f"Unknown command: {command_input}")
                    print(f"Unknown command: {command_input}")
        except KeyboardInterrupt:
            logging.info("Application interrupted, exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()
