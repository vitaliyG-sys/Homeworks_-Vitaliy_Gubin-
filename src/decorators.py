from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Any:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Принимает необязательный аргумент "filename",
    который определяет, куда будут записываться логи (в файл или в консоль)."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Блок выполнения кода, записывает лог в зависимости от параметра filename.
            try:
                func(*args, **kwargs)
                if not filename:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"\n{func.__name__} ok")
            # Блок отлова ошибки, записывает лог в зависимости от параметра filename.
            except Exception as error_text:
                if not filename:
                    print(f"{func.__name__} error: {error_text}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"\n{func.__name__} error: {error_text}. Inputs: {args}, {kwargs}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
