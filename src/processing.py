def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа "state" (по умолчанию "EXECUTED")
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    sorted_operations = []
    # Условия проверяют корректность типа переданных аргументов.
    if not isinstance(operations, list):
        raise TypeError("operations must be a list")
    elif not all(isinstance(operation, dict) for operation in operations):
        raise TypeError("operation must be a dict")

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
        # Условие проверяет правильность переданного формата даты.
        elif len(operation["date"]) < 21 or "".join(x for x in operation["date"] if not x.isdigit()) != "--T::.":
            raise ValueError("неверный формат даты")
    # Сортировка списка по дате.
    return sorted(operations, key=lambda operation_dt: operation_dt["date"], reverse=order)
