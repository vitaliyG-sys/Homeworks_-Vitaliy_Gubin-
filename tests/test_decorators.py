import re
from typing import Any

import pytest

from src.decorators import log


def test_log_with_filename() -> None:
    """1. Проверяет работу декоратора с указанным параметром "filename"."""

    @log(filename="mylog.txt")
    def my_function(x: int | float, y: int | float) -> int | float:
        """ Тестовая функция, складывающая 2 числа."""
        return x + y

    assert my_function(1, 2) == 3


def test_log_without_filename() -> None:
    """2. Проверяет работу декоратора без указанного параметра "filename"."""

    @log()
    def my_function(x: int | float, y: int | float) -> int | float:
        """ Тестовая функция, произведение двух чисел."""
        return x * y

    assert my_function(5, 6) == 30


def test_log_console_logging(capsys: pytest.CaptureFixture[str]) -> None:
    """3. Проверяет корректность записи в консоль."""

    @log()
    def my_function(x: int | float, y: int | float) -> int | float:
        """ Тестовая функция, произведение двух чисел."""
        return x * y

    my_function(1, 2)
    captured = capsys.readouterr()
    # Проверка вывода в консоль
    assert captured.out == "my_function ok\n"
    assert captured.err == ""

# Параметризация тестов с некорректными типами данных в аргументах для передачи в функцию "test_log_error".
@pytest.mark.parametrize(
    "incorrect_data_x, incorrect_data_y ,error_message",
    [
        (1, 0, "division by zero"),
        (1, "2", "unsupported operand type(s) for /: 'int' and 'str'"),
        (1, (2, 3), "unsupported operand type(s) for /: 'int' and 'tuple'"),
        (None, 2, "unsupported operand type(s) for /: 'NoneType' and 'int'"),
    ],
)
def test_log_error(
    incorrect_data_x: int | bool | float, incorrect_data_y: Any, error_message: str
) -> None:
    """4. Проверяет обработку исключений декоратора."""

    # Проверка работы декоратора с указанным параметром "filename".
    @log(filename="mylog.txt")
    def my_function(x: int | float, y: int | float) -> int | float:
        """ Тестовая функция, деления двух чисел."""
        return x / y

    with pytest.raises(Exception, match=re.escape(error_message)):
        my_function(incorrect_data_x, incorrect_data_y)

    # Проверка работы декоратора без указанного параметра "filename".
    @log()
    def my_function(x: int | float, y: int | float) -> int | float:
        """ Тестовая функция, деления двух чисел."""
        return x / y

    with pytest.raises(Exception, match=re.escape(error_message)):
        my_function(incorrect_data_x, incorrect_data_y)