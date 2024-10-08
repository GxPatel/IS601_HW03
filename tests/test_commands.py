''' test_commands.py '''
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command(monkeypatch, capfd):
    ''' testing add command '''
    monkeypatch.setattr('builtins.input', lambda _: '5')
    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 10" in out

def test_subtract_command(monkeypatch, capfd):
    ''' testing subtract command '''
    monkeypatch.setattr('builtins.input', lambda _: '5')
    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 0" in out

def test_multiply_command(monkeypatch, capfd):
    ''' testing multiply command '''
    monkeypatch.setattr('builtins.input', lambda _: '5')
    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 25" in out

def test_divide_by_zero(monkeypatch, capfd):
    ''' testing divide command '''
    monkeypatch.setattr('builtins.input', lambda _: '0')
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Error: Division by zero" in out
