from datetime import datetime as dt

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """
    Функция принимает название и номер счета или карты, вызывает функцию "get_mask_card_number" или "get_mask_account"
    в зависимости от типа данных и возвращает название с замаскированным номером
    """
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(account_or_card_number, str):
        raise TypeError("account_or_card_number must be a string")

    # Разделяем номер и название объекта.
    object_number = "".join(c for c in account_or_card_number if c.isdigit())
    object_type = "".join(c for c in account_or_card_number if not c.isdigit())

    # Условие проверяет наличие номера карты или счета в переданном аргументе.
    if object_number == "":
        raise ValueError("Введите номер счета или карты")
    # Условия вызывают функцию маскировки номера счета или карты, возвращает отформатированный результат.
    elif len(object_number) == 16:
        masked = get_mask_card_number(object_number)
        return f"{object_type + masked}"
    elif len(object_number) == 20:
        masked = get_mask_account(object_number)
        return f"{object_type + masked}"
    # Условие возвращает ошибку если в аргументах неправильные форматы номеров счета или карты.
    else:
        raise ValueError("Неправильный номер счета или карты")


def get_date(iso_date: str) -> str:
    """
    Функция принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(iso_date, str):
        raise TypeError("iso_date must be a string")
    # Условие проверяет наличие даты в переданном аргументе.
    elif iso_date == "":
        raise ValueError("не указана дата операции")
    # Условие проверяет правильность переданного формата даты.
    elif len(iso_date) < 21 or "".join(x for x in iso_date if not x.isdigit()) != "--T::.":
        raise ValueError("неверный формат даты")
    try:
        # Форматирует строку в datetime
        date_time = dt.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_time.strftime("%d.%m.%Y")
    # Исключение для некорректных календарных значений.
    except ValueError:
        raise ValueError("Неверные календарные значения")
