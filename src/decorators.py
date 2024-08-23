from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует вызов функции и ее результат в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            try:
                result == sum(args)
                filename.write("my_function ok")
                print("my_function ok")
            except Exception as e:
                filename.write(f"my_function error: {e}. Inputs:{args}, {kwargs}")
                print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function("1", "2")


