from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_or_card_number : str) -> str:
    """
    Функция принимает название и номер счета или карты, вызывает функцию "get_mask_card_number" или "get_mask_account"
    в зависимости от типа данных и возвращает название с замаскированным номером
    """
    # Разделяем номер и название объекта.
    object_number = "".join(x for x in account_or_card_number if x.isdigit())
    object_type = "".join(x for x in account_or_card_number if not x.isdigit())

    # Вызываем функцию маскировки номера счета/карты, возвращаем отформатированный результат.
    if len(object_number) == 16:
        masked = get_mask_card_number(object_number)
        return object_type + masked
    elif len(object_number) == 20:
        masked = get_mask_account(object_number)
        return object_type + masked

    return "Invalid account number"


#Тестовые данные
test = ["Maestro 1596837868705199", "Счет 64686473678894779589", "MasterCard 7158300734726758",
        "Счет 35383033474447895560", "Visa Classic 6831982476737658", "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353", "Счет 73654108430135874305"]
for x in test:
    print(mask_account_card(x))