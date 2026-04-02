import logging
import os

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log")
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты и возвращает в формате 'XXXX XX** **** XXXX'.
    """
    logger.debug("Запуск функции 'get_mask_card_number'")
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(card_number, str):
        logger.error("card_number must be a string")
        raise TypeError("card_number must be a string")
    # Условие проверяет наличие номера карты в переданном аргументе.
    elif card_number == "":
        logger.error("Введите номер карты")
        raise ValueError("Введите номер карты")
    # Условие проверяет корректность формата номера карты.
    elif not card_number.isdigit() or len(card_number) != 16:
        logger.error("Неправильный номер карты")
        raise ValueError("Неправильный номер карты")
    logger.debug("Завершение работы функции 'get_mask_card_number'")
    # Маскировка номера карты.
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер аккаунта и возвращает в формате '**XXXX'.
    """
    logger.debug("Запуск функции 'get_mask_account'")
    # Условие проверяет корректность типа переданных аргументов.
    if not isinstance(account_number, str):
        logger.error("account_number must be a string")
        raise TypeError("account_number must be a string")
    # Условие проверяет наличие номера счета в переданном аргументе.
    elif account_number == "":
        logger.error("Введите номер счета")
        raise ValueError("Введите номер счета")
    # Условие проверяет корректность формата номера счета.
    elif not account_number.isdigit() or len(account_number) != 20:
        logger.error("Неправильный номер счета")
        raise ValueError("Неправильный номер счета")
    logger.debug("Завершение работы функции 'get_mask_account'")
    # Маскировка номера счета.
    return f"**{account_number[-4:]}"
