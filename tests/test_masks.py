from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_get_mask_card_number_correct_value(correct_card_number: str, expected_masked_card_number: str) -> None:
    """1. Проверяет работу функции "get_mask_card_number" с корректно введенными данными."""
    assert get_mask_card_number(correct_card_number) == expected_masked_card_number


# Параметризация для передачи в функцию get_mask_card_number,
# содержащий символы, буквы, пробелы и неверное количество цифр.
@pytest.mark.parametrize(
    "incorrect_card_number",
    [
        "a1234567890123456",
        "1234 5678 9012 3456",
        "12345678901234567",
        "123456789012",
        "1234 5678.9012 3456",
        "1234 5678 9012 3456\n",
    ],
)
def test_get_mask_card_number_incorrect_data(incorrect_card_number: str) -> None:
    """2. Проверяет работу функции "get_mask_card_number" с неверно введенными данными."""
    with pytest.raises(ValueError, match="Неправильный номер карты"):
        get_mask_card_number(incorrect_card_number)


def test_get_mask_card_number_empty_data(empty_data: str = "") -> None:
    """3. Проверяет работу функции "get_mask_card_number" с пустыми данными."""
    with pytest.raises(ValueError, match="Введите номер карты"):
        get_mask_card_number(empty_data)


# Параметризация для передачи в функцию get_mask_card_number, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_type_of_card_number",
    [1234567890123456, ["1234 5678 9012 3456"], {"1234 5678 9012 3456"}, None, False, True],
)
def test_get_mask_card_number_incorrect_data_type(incorrect_type_of_card_number: Any) -> None:
    """4. Проверяет работу функции "get_mask_card_number" с неправильным типом данных."""
    with pytest.raises(TypeError, match="card_number must be a string"):
        get_mask_card_number(incorrect_type_of_card_number)


def test_get_mask_account_correct_value(correct_account_number: str, expected_masked_account_number: str) -> None:
    """5. Проверяет работу функции "get_mask_account" с корректно введенными данными."""
    assert get_mask_account(correct_account_number) == expected_masked_account_number


# Параметризация для передачи в функцию get_mask_account,
# содержащий символы, буквы, пробелы и неверное количество цифр.
@pytest.mark.parametrize(
    "incorrect_account_number",
    [
        "s1234567890123456789",
        "12345678901234567890 ",
        "12345678901234567890\n",
        "1234567890123456",
        "123456789012345678901",
    ],
)
def test_get_mask_account_incorrect_data(incorrect_account_number: str) -> None:
    """6. Проверяет работу функции "get_mask_account" с неверно введенными данными."""
    with pytest.raises(ValueError, match="Неправильный номер счета"):
        get_mask_account(incorrect_account_number)


def test_get_mask_account_empty_data(empty_data: str = "") -> None:
    """7. Проверяет работу функции "get_mask_account" с пустыми данными."""
    with pytest.raises(ValueError, match="Введите номер счета"):
        get_mask_account(empty_data)


# Параметризация для передачи в функцию get_mask_account, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_type_of_account_number",
    [12345678901234567890, ["12345678901234567890"], {"12345678901234567890"}, None, False, True],
)
def test_get_mask_account_incorrect_data_type(incorrect_type_of_account_number: Any) -> None:
    """8. Проверяет работу функции "get_mask_account" с неправильным типом данных."""
    with pytest.raises(TypeError, match="account_number must be a string"):
        get_mask_account(incorrect_type_of_account_number)
