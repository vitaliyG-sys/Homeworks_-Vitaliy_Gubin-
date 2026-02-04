def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты и возвращает в формате 'XXXX XX** **** XXXX'.
    """
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(card_number, str):
        raise TypeError("card_number must be a string")
    # Условие проверяет наличие номера карты в переданном аргументе.
    elif card_number == "":
        raise ValueError("Введите номер карты")
    # Условие проверяет корректность формата номера карты.
    elif not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Неправильный номер карты")
    # Маскировка номера карты.
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер аккаунта и возвращает в формате '**XXXX'.
    """
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(account_number, str):
        raise TypeError("account_number must be a string")
    # Условие проверяет наличие номера счета в переданном аргументе.
    elif account_number == "":
        raise ValueError("Введите номер счета")
    # Условие проверяет корректность формата номера счета.
    elif not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Неправильный номер счета")
    # Маскировка номера счета.
    return f"**{account_number[-4:]}"
