from typing import Any

import pytest

from src.widget import get_date, mask_account_card


# Параметризация для передачи корректных данных в функцию mask_account_card.
@pytest.mark.parametrize(
    "correct_card_or_account_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_correct_value(correct_card_or_account_number: str, expected: str) -> None:
    """1. Проверяет работу функции "mask_account_card" с корректно введенными данными."""
    assert mask_account_card(correct_card_or_account_number) == expected


def test_mask_account_card_empty_data(empty_data: str = "") -> None:
    """2. Проверяет работу функции "mask_account_card" с пустыми данными."""
    with pytest.raises(ValueError, match="Введите номер счета или карты"):
        mask_account_card(empty_data)


# Параметризация для передачи некорректных данных в функцию mask_account_card.
@pytest.mark.parametrize(
    "incorrect_card_or_account_number",
    [
        "Maestro 01596837868705199",
        "MasterCard 71583007347267589",
        "Счет 6468647367889475678",
        "Счет 353830334744478955601",
    ],
)
def test_mask_account_card_incorrect_value(incorrect_card_or_account_number: str) -> None:
    """3. Проверяет работу функции "mask_account_card" с некорректно введенными данными."""
    with pytest.raises(ValueError, match="Неправильный номер счета или карты"):
        mask_account_card(incorrect_card_or_account_number)


# Параметризация для передачи в функцию mask_account_card, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type",
    [
        ("id", "state", "date"),
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        12345678901234567890,
        None,
        True,
    ],
)
def test_mask_account_card_incorrect_data_type(incorrect_data_type: Any) -> None:
    """4. Проверяет работу функции "mask_account_card" с неправильным типом данных."""
    with pytest.raises(TypeError, match="account_or_card_number must be a string"):
        mask_account_card(incorrect_data_type)


# Параметризация для передачи корректных данных в функцию get_date.
@pytest.mark.parametrize(
    "correct_date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2019-07-03T18:35:29.5", "03.07.2019")]
)
def test_get_date_correct_value(correct_date: str, expected: str) -> None:
    """5. Проверяет работу функции "get_date" с корректно введенными данными."""
    assert get_date(correct_date) == expected


def test_get_date_empty_data(empty_data: str = "") -> None:
    """6. Проверяет работу функции "get_date" с пустыми данными."""
    with pytest.raises(ValueError, match="не указана дата операции"):
        get_date(empty_data)


# Параметризация для передачи некорректных данных в функцию get_date.
@pytest.mark.parametrize("incorrect_date", ["02/02/2010 19:44", "2019-07-03T18:35:29"])
def test_get_date_incorrect_value(incorrect_date: str) -> None:
    """7. Проверяет работу функции "get_date" с некорректно введенными данными."""
    with pytest.raises(ValueError, match="неверный формат даты"):
        get_date(incorrect_date)


# Параметризация для передачи в функцию get_date, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type",
    [
        ("id", "state", "date"),
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        12345678901234567890,
        None,
        True,
    ],
)
def test_get_date_incorrect_data_type(incorrect_data_type: Any) -> None:
    """8. Проверяет работу функции "get_date" с неправильным типом данных."""
    with pytest.raises(TypeError, match="iso_date must be a string"):
        get_date(incorrect_data_type)


# Параметризация для передачи в функцию get_date с неправильными значениями календаря.
@pytest.mark.parametrize(
    "incorrect_calendar_values",
    [
        "32018-09-12T21:27:25.241689",
        "2018-13-29T21:27:25.241689",
        "2018-13-32T21:27:25.241689",
        "2018-09-12T25:27:25.241689",
        "2018-09-12T21:61:25.241689",
        "2018-09-12T21:27:61.241689",
    ],
)
def test_get_date_incorrect_calendar_values(incorrect_calendar_values: str) -> None:
    """9. Проверяет работу функции "get_date" с неправильными значениями календаря."""
    with pytest.raises(ValueError, match="Неверные календарные значения"):
        get_date(incorrect_calendar_values)
