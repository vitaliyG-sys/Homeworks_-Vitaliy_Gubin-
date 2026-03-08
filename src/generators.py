from typing import Generator


def filter_by_currency(operations: list[dict], currency: str) -> Generator[dict, None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    # Условие возвращает ошибку если на вход передан пустой список.
    if not operations:
        raise ValueError("Веден пустой список")
    for operation in operations:
        # Условие проверяет наличие ключей 'code', 'currency' и 'operationAmount' во вложенных словарях.
        if (
            not operation.get("operationAmount", {}).get("currency", {}).get("code", {})
            or not operation.get("operationAmount", {}).get("currency", {})
            or not operation.get("operationAmount", {})
        ):
            raise KeyError("Отсутствуют данные по валютным операциям")
        # Условие возвращает объект по заданной валюте.
        elif operation.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
            yield operation


def transaction_descriptions(operations: list[dict]) -> Generator[str, None, None]:
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    # Условие возвращает ошибку если на вход передан пустой список.
    if not operations:
        raise ValueError("Веден пустой список")
    for operation in operations:
        # Условие возвращает ошибку если количество запросов превышает количество объектов в списке.
        if operation == operations[-1]:
            yield operation["description"]
            raise ValueError("Итерация завершена")
        # Возвращает описания операций.
        yield operation["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """
    # Условие проверяет корректность диапазона переданных значений.
    if start < 1 or stop > 9999999999999999:
        raise ValueError("Неверный диапазон номеров карт")
    # Итератор генерирует номера карт.
    for x in range(start, stop + 1):
        d = str(x).zfill(16)
        yield f"{d[:4]} {d[4:8]} {d[8:12]} {d[12:]}"
