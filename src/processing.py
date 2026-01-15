def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция принимает список словарей и возвращает
    список словарей со значением ключа state:"EXECUTED" """
    executed_operations = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            executed_operations.append(operation)
            continue