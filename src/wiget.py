from datetime import datetime as dt

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """
    Функция принимает название и номер счета или карты, вызывает функцию "get_mask_card_number" или "get_mask_account"
    в зависимости от типа данных и возвращает название с замаскированным номером
    """

    # Разделяем номер и название объекта.
    object_number = "".join(c for c in account_or_card_number if c.isdigit())
    object_type = "".join(c for c in account_or_card_number if not c.isdigit())

    # Вызываем функцию маскировки номера счета/карты, возвращаем отформатированный результат.
    if len(object_number) == 16:
        masked = get_mask_card_number(object_number)
        return f"{object_type + masked}"
    elif len(object_number) == 20:
        masked = get_mask_account(object_number)
        return f"{object_type + masked}"

    return "Invalid account number"


def get_date(iso_date: str) -> str:
    """
    Функция которая принимает строку с датой формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    # Форматируем строку в datetime
    date_time = dt.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%f")
    # Возвращаем строку в нужном формате
    return date_time.strftime("%d.%m.%Y")
