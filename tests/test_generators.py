import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_correct_value(correct_transactions_for_generators: list[dict]) -> None:
    """1. Проверяет работу функции "filter_by_currency" с корректно заданной валютой включая случаи,
    когда валюта отсутствует."""
    assert len(list(filter_by_currency(correct_transactions_for_generators, "USD"))) == 3
    assert len(list(filter_by_currency(correct_transactions_for_generators, "RUB"))) == 2
    assert len(list(filter_by_currency(correct_transactions_for_generators, "JPY"))) == 0


def test_filter_by_currency_empty_data(correct_transactions_for_generators: list[dict]) -> None:
    """2. Проверяет работу функции "filter_by_currency" с пустыми данными."""
    with pytest.raises(ValueError, match="Веден пустой список"):
        next(filter_by_currency([], "RUB"))


# Параметризация тестов для передачи в функцию "filter_by_currency" с отсутствующими валютными операциями.
@pytest.mark.parametrize(
    "incorrect_operations",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07"},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб."}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            {
                "id": 873106800,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
        ]
    ],
)
def test_filter_by_currency_missing_currency(incorrect_operations: list[dict]) -> None:
    """3. Проверяет работу функции "filter_by_currency" если есть список без соответствующих валютных операций."""
    with pytest.raises(KeyError, match="Отсутствуют данные по валютным операциям"):
        next(filter_by_currency(incorrect_operations, "RUB"))


def test_transaction_descriptions_correct_value(correct_transactions_for_generators: list[dict]) -> None:
    """4. Проверяет работу функции "transaction_descriptions" с корректно введенными данными и превышением запросов."""
    test_func = transaction_descriptions(correct_transactions_for_generators)
    assert next(test_func) == "Перевод организации"
    assert next(test_func) == "Перевод со счета на счет"
    assert next(test_func) == "Перевод со счета на счет"
    assert next(test_func) == "Перевод с карты на карту"
    assert next(test_func) == "Перевод организации"
    with pytest.raises(ValueError, match="Итерация завершена"):
        next(test_func)


def test_transaction_descriptions_empty_value() -> None:
    """5. Проверяет работу функции "transaction_descriptions" с пустым списком."""
    with pytest.raises(ValueError, match="Веден пустой список"):
        next(transaction_descriptions([]))


@pytest.mark.parametrize(
    "expected_numbers",
    [
        (
            "0000 0000 0000 0052",
            "0000 0000 0000 0053",
            "0000 0000 0000 0054",
            "0000 0000 0000 0055",
            "0000 0000 0000 0056",
            "0000 0000 0000 0057",
            "0000 0000 0000 0058",
        )
    ],
)
def test_card_number_generator_correct_value(expected_numbers: tuple[str, str]) -> None:
    """6. Проверяет работу функции "card_number_generator" на корректность номеров карт в заданном диапазоне
    и корректность форматирования карт."""
    test_func = card_number_generator(52, 58)
    for x in range(7):
        assert next(test_func) == expected_numbers[x]


def test_card_number_generator_boundary_cases() -> None:
    """7. Проверяет работу функции "card_number_generator" на соблюдение граничных случаев диапазона номеров карт."""
    with pytest.raises(ValueError, match="Неверный диапазон номеров карт"):
        next(card_number_generator(0, 12))
    with pytest.raises(ValueError, match="Неверный диапазон номеров карт"):
        next(card_number_generator(9999999999999980, 10000000000000000))
