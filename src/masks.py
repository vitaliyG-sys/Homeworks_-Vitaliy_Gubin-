def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты и возвращает в формате 'XXXX XX** **** XXXX'.
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер аккаунта и возвращает в формате '**XXXX'.
    """
    return f"**{account_number[-4:]}"
