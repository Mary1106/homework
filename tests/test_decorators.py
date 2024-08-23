import pytest
from src.decorators import log, my_function

def test_log_error(capsys):
    filename = "../logs/mylog.txt"
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == f"my_function is not ok: {error}. Inputs:{args}, {kwargs}\n"
    @log
    def my_function(x = "1", y = 1):
        return x + y

def test_log_ok(capsys):
    filename = "../logs/mylog.txt"
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == f"my_function is ok\n"
    @log
    def my_function(x = 1, y = 1):
        return x + y