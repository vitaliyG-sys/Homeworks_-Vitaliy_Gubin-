def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает
    список словарей со значением ключа state:"EXECUTED" """
    executed_operations = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            executed_operations.append(operation)
            continue
    return executed_operations


def sort_by_date(operations: list[dict]) -> list[dict]:
    """Функция принимает список словарей и возвращает
    список словарей отсортированный по дате в порядке убывания"""
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)
