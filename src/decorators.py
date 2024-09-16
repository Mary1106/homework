from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Логирует вызов функции и ее результат в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        def _log_result(message: str) -> None:
            if filename is not None:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{message}\n")
            else:
                print(message)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            """Обрабатываем исключения"""
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                log_message = f"{func.__name__} is not ok: {type(error).__name__}. Inputs:{args}, {kwargs}"
                _log_result(log_message)
                raise
            else:
                log_message = f"{func.__name__} is ok: {func(*args, **kwargs)}"
                _log_result(log_message)
                return result
        return wrapper

    return decorator
