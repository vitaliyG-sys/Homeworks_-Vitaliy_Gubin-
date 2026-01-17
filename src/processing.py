def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа "state" (по умолчанию "EXECUTED")
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    sorted_operations = []
    for operation in operations:
        if operation.get("state") == state:
            sorted_operations.append(operation)
    return sorted_operations


def sort_by_date(operations: list[dict], order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате"""
    return sorted(operations, key=lambda operation: operation["date"], reverse=order)
