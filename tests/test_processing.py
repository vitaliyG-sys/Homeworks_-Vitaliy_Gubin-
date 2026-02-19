from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_correct_value(
    filter_by_state_correct_data: list[dict],
    filter_by_state_expected_state_executed: list[dict],
    filter_by_state_expected_state_canceled: list[dict],
) -> None:
    """1. Проверяет работу функции "filter_by_state" с корректно введенными данными и
    параметрами  state: "по умолчанию", "EXECUTED" и "CANCELED"."""
    assert filter_by_state(filter_by_state_correct_data) == filter_by_state_expected_state_executed
    assert filter_by_state(filter_by_state_correct_data, state="EXECUTED") == filter_by_state_expected_state_executed
    assert filter_by_state(filter_by_state_correct_data, state="CANCELED") == filter_by_state_expected_state_canceled


# Параметризация тестов для передачи в функцию "filter_by_state" различных возможных значений статуса.
@pytest.mark.parametrize(
    "input_incorrect_state_value",
    [
        [
            {"id": 1234, "state": "EXAMPLE1", "date": "2011-07-03T22:35:29.512364"},
            {"id": 5678, "state": "REJECTED", "date": "2018-10-14T08:21:33.419441"},
        ],
        [
            {"id": 9012, "state": "EXAMPLE2", "date": "2019-07-03T18:35:29.512364"},
            {"id": 3456, "state": "PROCESSING", "date": "2018-10-14T08:21:33.419441"},
        ],
    ],
)
def test_filter_by_state_incorrect_state(input_incorrect_state_value: list[dict]) -> None:
    """2. Проверяет работу функции "filter_by_state" с параметром state не указанным в ТЗ."""
    assert filter_by_state(input_incorrect_state_value, state="CANCELED") == []
    assert filter_by_state(input_incorrect_state_value) == []


# Параметризация для передачи в функцию filter_by_state, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type_list",
    [
        ("id", "state", "date"),
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        12345678901234567890,
        None,
        True,
    ],
)
def test_filter_by_state_incorrect_data_type_list(incorrect_data_type_list: Any) -> None:
    """3. Проверяет работу функции "filter_by_state" с неправильным типом данных 'list'."""
    with pytest.raises(TypeError, match="operations must be a list"):
        filter_by_state(incorrect_data_type_list)


# Параметризация для передачи в функцию filter_by_state, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type_dict",
    [
        ["1234", "5678", "9012", "3456"],
        [1234, 5678, 9012, 3456],
        [(1234, 2), (5678, 4), (9012, 6), (7, 3456)],
        ["1234", 5678, (9012, 2), {"state": "EXECUTED"}],
        [{"state": "CANCELED"}, [3456], 5678],
    ],
)
def test_filter_by_state_incorrect_data_type_dict(incorrect_data_type_dict: Any) -> None:
    """4. Проверяет работу функции "filter_by_state" с неправильным типом данных  'dict'."""
    with pytest.raises(TypeError, match="operation must be a dict"):
        filter_by_state(incorrect_data_type_dict)


def test_sort_by_date_correct_value(
    filter_by_state_correct_data: list[dict],
    expected_sorted_by_date_bool_true: list[dict],
    expected_sorted_by_date_bool_false: list[dict],
) -> None:
    """5. Проверяет работу функции "sort_by_date" с корректно введенными данными и
    параметрами  order: "по умолчанию", "True" и "False"."""
    assert sort_by_date(filter_by_state_correct_data) == expected_sorted_by_date_bool_true
    assert sort_by_date(filter_by_state_correct_data, True) == expected_sorted_by_date_bool_true
    assert sort_by_date(filter_by_state_correct_data, False) == expected_sorted_by_date_bool_false


# Параметризация для передачи в функцию filter_by_state, с некорректными или нестандартными форматами дат.
@pytest.mark.parametrize(
    "incorrect_date_format",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        ],
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2025-04-09 19:44:50"},
        ],
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "14-10-2019 18:43"},
        ],
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "14/10/2023"},
        ],
    ],
)
def test_sort_by_date_incorrect_value(incorrect_date_format: list[dict]) -> None:
    """6. Проверяет работу функции "sort_by_date" с некорректными или нестандартными форматами дат."""
    with pytest.raises(ValueError, match="неверный формат даты"):
        sort_by_date(incorrect_date_format)


# Параметризация для передачи в функцию sort_by_date, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type_list",
    [
        ("id", "state", "date"),
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        12345678901234567890,
        None,
        True,
    ],
)
def test_sort_by_date_incorrect_data_type_list(incorrect_data_type_list: Any) -> None:
    """7. Проверяет работу функции "sort_by_date" с неправильным типом данных 'list'."""
    with pytest.raises(TypeError, match="operations must be a list"):
        sort_by_date(incorrect_data_type_list)


# Параметризация для передачи в функцию filter_by_state, с неправильными типами данных.
@pytest.mark.parametrize(
    "incorrect_data_type_dict",
    [
        ["1234", "5678", "9012", "3456"],
        [1234, 5678, 9012, 3456],
        [(1234, 2), (5678, 4), (9012, 6), (7, 3456)],
        ["1234", 5678, (9012, 2), {"state": "EXECUTED"}],
        [{"state": "CANCELED"}, [3456], 5678],
    ],
)
def test_sort_by_date_incorrect_data_type_dict(incorrect_data_type_dict: Any) -> None:
    """8. Проверяет работу функции "sort_by_date" с неправильным типом данных 'dict'."""
    with pytest.raises(TypeError, match="operation must be a dict"):
        sort_by_date(incorrect_data_type_dict)


# Параметризация для передачи в функцию sort_by_date, с пустым значением ключа 'date'.
@pytest.mark.parametrize(
    "empty_date_value",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": ""},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ],
)
def test_sort_by_date_empty_date_value(empty_date_value: list[dict]) -> None:
    """9. Проверяет работу функции "sort_by_date" с пустыми данными."""
    with pytest.raises(ValueError, match="не указана дата операции"):
        sort_by_date(empty_date_value)


# Параметризация для передачи в функцию sort_by_date, с отсутствием ключа 'date'.
@pytest.mark.parametrize(
    "no_key_date",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ],
)
def test_sort_by_date_no_key_date(no_key_date: list[dict]) -> None:
    """10. Проверяет работу функции "sort_by_date" с отсутствующим ключом 'date'."""
    with pytest.raises(ValueError, match="operation must have 'date' key"):
        sort_by_date(no_key_date)
