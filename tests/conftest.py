import pytest


# Фикстура возвращает пример корректного ввода для тестирования корректной работы функции "get_mask_card_number"
@pytest.fixture
def correct_card_number() -> str:
    return "1234567890123456"


# Фикстура возвращает пример результата для тестирования корректной работы функции "get_mask_card_number"
@pytest.fixture
def expected_masked_card_number() -> str:
    return "1234 56** **** 3456"


# Фикстура возвращает пример корректного ввода для тестирования корректной работы функции "get_mask_account"
@pytest.fixture
def correct_account_number() -> str:
    return "12345678901234567890"


# Фикстура возвращает пример результата для тестирования корректной работы функции "get_mask_account"
@pytest.fixture
def expected_masked_account_number() -> str:
    return "**7890"


# Фикстура возвращает пример корректного ввода для тестирования корректной работы функции "filter_by_state"
@pytest.fixture
def filter_by_state_correct_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура возвращает пример результата для тестирования корректной работы функции "filter_by_state"
# c параметром state = "EXECUTED"
@pytest.fixture
def filter_by_state_expected_state_executed() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Фикстура возвращает пример результата для тестирования корректной работы функции "filter_by_state"
# c параметром state = "CANCELED"
@pytest.fixture
def filter_by_state_expected_state_canceled() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура возвращает пример результата для тестирования корректной работы функции "sort_by_date"
# c параметром order = True
@pytest.fixture
def expected_sorted_by_date_bool_true() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Фикстура возвращает пример результата для тестирования корректной работы функции "sort_by_date"
# c параметром order = False
@pytest.fixture
def expected_sorted_by_date_bool_false() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Фикстура возвращает пример корректного ввода для тестирования корректной работы функции "get_mask_card_number"
@pytest.fixture
def correct_card_or_account_number() -> list:
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]
