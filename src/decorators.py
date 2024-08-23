from functools import wraps
from typing import Any, Callable


def log(filename: str | None) -> Callable:
    """Логирует вызов функции и ее результат в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обрабатываем исключения"""
            try:
                func(*args, **kwargs)
            except Exception as error:
                log_message = f"my_function is not ok: {error}. Inputs:{args}, {kwargs}"
            else:
                log_message = f"my_function is ok"

            """Смотрим, куда отправить лог"""
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{log_message}\n")
            else:
                print(log_message)
            return
        return wrapper
    return decorator


@log(filename="../logs/mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function("1", 2))
