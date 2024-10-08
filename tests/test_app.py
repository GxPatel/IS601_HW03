'''test_app.py'''
import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    ''' app testing for start and exit commands '''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_unknown_command(capfd, monkeypatch):
    ''' app testing for input commands '''
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
