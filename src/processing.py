import re
from collections import Counter
from itertools import chain


def filter_by_state(operations: list[dict] , state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа "state" (по умолчанию "EXECUTED")
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    sorted_operations = []

    # Перебор входящего списка и заполнение нового в соответствии с ключом 'state'.
    for operation in operations:
        if operation.get("state") == state:
            sorted_operations.append(operation)
    return sorted_operations


def sort_by_date(operations: list[dict], order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате"""

    # Условия проверяют корректность типа переданных аргументов.
    if not isinstance(operations, list):
        raise TypeError("operations must be a list")
    elif not all(isinstance(operation, dict) for operation in operations):
        raise TypeError("operation must be a dict")

    for operation in operations:
        # Условие проверяет наличие ключа 'date' в списке.
        if "date" not in operation:
            raise ValueError("operation must have 'date' key")
        # Условие проверяет наличие даты по ключу 'date' в списке.
        elif operation["date"] == "":
            raise ValueError("не указана дата операции")
    # Сортировка списка по дате.
    return sorted(operations, key=lambda operation_dt: operation_dt["date"], reverse=order)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    sorted_list = []
    if not search:
        print("Строка поиска не заполнена")
        return data

    # Перебор входящего списка "data" и заполнение нового в соответствии с ключом 'state'.
    for operation in data:
        search_data = re.search(search, operation.get("description", ""), flags=re.IGNORECASE)
        if search_data:
            sorted_list.append(operation)
    return sorted_list


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    # Список транзакций, с указанными в аргументах категориями.
    sorted_list_by_categories = list(chain.from_iterable(process_bank_search(data, x) for x in categories))
    categories_list = []  # Список категорий в транзакциях.
    id_list = []  # Список id в транзакциях.
    # Фильтрация дубликатов транзакций. Заполнение списка категорий в транзакциях.
    for operation in sorted_list_by_categories:
        if operation.get("id", {}) in id_list:
            continue
        else:
            categories_list.append(operation.get("description", {}))
            id_list.append(operation.get("id", {}))
    return Counter(categories_list)
