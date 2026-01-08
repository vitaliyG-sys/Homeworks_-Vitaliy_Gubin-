def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты, проверяет правильность введенных данных
    и возвращает в формате 'XXXX XX** **** XXXX'.
    Проверяет правильность введенных данных с выводом ошибки.
    """

    # Удаляем пробелы из полученных данных
    cleared_card_number = card_number.replace(" ", "")

    # Проверяем правильность введенных данных с выводом ошибки
    if len(cleared_card_number) != 16 or not cleared_card_number.isdigit():
        raise ValueError("Invalid card number")
    return f"{cleared_card_number[:4]} {cleared_card_number[4:6]}** **** {cleared_card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер аккаунта, проверяет правильность введенных данных
    и возвращает в формате '**XXXX'.
    Проверяет правильность введенных данных с выводом ошибки.
    """

    # Удаляем пробелы из полученных данных
    cleared_account_number = account_number.replace(" ", "")

    # Проверяем правильность введенных данных с выводом ошибки
    if len(cleared_account_number) != 20 or not account_number.isdigit():
        raise ValueError("Invalid account number")
    return f"**{cleared_account_number[-4:]}"
