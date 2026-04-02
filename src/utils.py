import json
import logging
import os
import typing
from typing import Any

from src.external_api import currency_conversion

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_json_file(path: typing.Union[str, os.PathLike]) -> list[Any] | list[dict] | Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    result = []
    logger.debug("Запуск функции 'get_json_file'")
    try:
        with open(path, "r", encoding="utf-8") as json_operations:
            result = json.load(json_operations)
        logger.debug(f"Загрузка файла: {os.path.basename(path)}")
    except FileNotFoundError as ex:
        logger.error("Файл не найден: %s", [ex])
        return result
    except json.JSONDecodeError as ex:
        logger.error("Ошибка декодирования файла: %s", [ex])
        return result
    logger.debug("Завершение работы функции 'get_json_file'")
    return result


def transaction_sum_in_rub(transactions: list | list[dict]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли."""
    logger.debug("Запуск функции 'transaction_sum_in_rub'")
    amount = []
    exchange_rate = {}

    if not transactions:
        logger.error("Отсутствует информация по транзакциям")
        raise ValueError("Отсутствует информация по транзакциям")

    # Получение валют из файла json для конвертации.
    currency_list = {
        x["operationAmount"]["currency"]["code"]
        for x in transactions
        if "operationAmount" in x and x["operationAmount"]["currency"]["code"] != "RUB"
    }
    # Заполнение словаря exchange_rate {валюта:курс на единицу} информацией по курсу валют в текущем списке транзакций.
    # Отправка запросов на https://api.apilayer.com через функцию currency_conversion.
    for currency_for_rate in currency_list:
        rate = currency_conversion(currency_for_rate)
        exchange_rate.update({currency_for_rate: rate})
        if not rate:
            logger.error("Ошибка конвертации валюты")
            raise ValueError("Ошибка конвертации валюты")

    # Заполнение списка amount транзакциями в рублях.
    for transaction in transactions:
        if "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] == "RUB":
            amount.append(float(transaction["operationAmount"]["amount"]))
        elif "operationAmount" in transaction and transaction["operationAmount"]["currency"]["code"] != "RUB":
            currency = transaction["operationAmount"]["currency"]["code"]
            converted_currency = float(transaction["operationAmount"]["amount"]) * float(exchange_rate[currency])
            amount.append(round(converted_currency, 2))
    logger.debug("Завершение работы функции 'transaction_sum_in_rub'")
    return sum(amount)
