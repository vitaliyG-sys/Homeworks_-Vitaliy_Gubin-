import json
import os
from unittest.mock import mock_open, patch, Mock

import pytest

from src.utils import get_json_file, transaction_sum_in_rub


def test_get_json_file_correct_data(correct_transactions_for_generators: list[dict]) -> None:
    """1. Проверяет работу функции "get_json_file" с корректно введенными данными."""
    # Задаём содержимое, которое «будет» в файле.
    content = json.dumps(correct_transactions_for_generators)
    # Создаём mock для open, передав содержимое через read_data.
    mock_file = mock_open(read_data=content)
    # Подменяем builtins.open на наш mock
    with patch("builtins.open", mock_file):
        assert get_json_file("dummy.json") == correct_transactions_for_generators


def test_get_json_file_not_found() -> None:
    """2. Проверяет работу функции "get_json_file" с обработкой ошибки FileNotFoundError."""
    invalid_path = os.path.abspath("invalid_path.json")
    assert get_json_file(invalid_path) == []


def test_get_json_file_decode_error() -> None:
    """3. Проверяет работу функции "get_json_file" с обработкой ошибки json.JSONDecodeError."""
    content = '{"name": "Боб", "age": 40,}'
    mock_file = mock_open(read_data=content)
    with patch("builtins.open", mock_file):
        assert get_json_file("dummy.json") == []


@patch("src.utils.currency_conversion")
def test_transaction_sum_in_rub_correct_value(mock_cc: Mock, correct_transactions_for_generators: list[dict]) -> None:
    """4. Проверяет работу функции "transaction_sum_in_rub" с корректно введенными данными."""
    mock_cc.return_value = "1"
    assert transaction_sum_in_rub(correct_transactions_for_generators) == 256455.58


@patch("src.utils.currency_conversion")
def test_transaction_sum_in_rub_no_rate(mock_cc: Mock, correct_transactions_for_generators: list[dict]) -> None:
    """5. Проверяет работу функции "transaction_sum_in_rub" c ошибкой конвертации валют."""
    mock_cc.return_value = None
    with pytest.raises(ValueError, match="Ошибка конвертации валюты"):
        transaction_sum_in_rub(correct_transactions_for_generators)


def test_transaction_sum_in_rub_empty_transactions() -> None:
    """6. Проверяет работу функции "transaction_sum_in_rub" с пустым списком в переданном аргументе."""
    with pytest.raises(ValueError, match="Отсутствует информация по транзакциям"):
        transaction_sum_in_rub([])
