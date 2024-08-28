from src.decorators import log


def test_log_not_ok(capsys):
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == ("my_function is not ok: unsupported operand type(s) for +: 'int' and 'str'. "
                            "Inputs:(1, '2'), {}\n")


def test_log_ok(capsys):
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function is ok\n"


def test_log_to_file(tmpdir):
    # Используем временный файл для логов
    log_file = tmpdir.join("test_log.txt")

    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    decorated_func = log(log_file.strpath)(my_function)

    decorated_func(1, 2)

    with open(log_file.strpath, 'r') as f:
        content = f.read()

    expected_content = "my_function is ok\n"
    assert content == expected_content
