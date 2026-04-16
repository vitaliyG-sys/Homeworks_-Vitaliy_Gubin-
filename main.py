import os
from functools import wraps
from typing import Callable

from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_files import read_csv, read_excel
from src.utils import get_json_file
from src.widget import get_date, mask_account_card


def file_type_settings() -> list[dict]:
    """Функция запрашивает из какого формата файла будет составлен запрос.
    Считывает файл из папки "/data" в зависимости от выбора."""

    file_type = int(
        input(
            """ Выберите необходимый пункт меню: \n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n """
        )
    )
    if file_type == 1:
        print(" Для обработки выбран JSON-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        return get_json_file(path)
    elif file_type == 2:
        print(" Для обработки выбран CSV-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
        return read_csv(path)
    elif file_type == 3:
        print(" Для обработки выбран XLSX-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
        return read_excel(path)
    return []


def transaction_status(data: list[dict] ) -> list[dict]:
    """Функция запрашивает статус, по которому необходимо выполнить фильтрацию, "EXECUTED/CANCELED/PENDING".
    Затем фильтрует данные в зависимости от выбора."""
    status = input(
        """ Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n """
    ).upper()
    ds = ["EXECUTED", "CANCELED", "PENDING"]
    if str(status) in ds:
        result = filter_by_state(data, status)
        return result
    else:
        print(f"Статус операции '{status}' недоступен.")
        return transaction_status(data)


def transaction_sorted_by_date(data: list[dict]) -> list[dict]:
    """Функция запрашивает о необходимости сортировки по возрастанию или по убыванию "Да/Нет".
    При положительном ответе сортирует данные в зависимости от выбора."""

    def crease_setting() -> list | list[dict]:
        """Функция запрашивает какой использовать порядок сортировки "по возрастанию/по убыванию"."""
        crease = input("Отсортировать по возрастанию или по убыванию?")
        if crease.lower() == "по возрастанию":
            return sort_by_date(data, False)
        elif crease.lower() == "по убыванию":
            return sort_by_date(data)
        else:
            print("Введен неверный параметр: 'по возрастанию' или 'по убыванию'!")
            return crease_setting()

    choice_sort_settings = input("Отсортировать операции по дате? Да / Нет")
    if choice_sort_settings.lower() == "нет":
        return sort_by_date(data)
    elif choice_sort_settings.lower() == "да":
        return crease_setting()
    else:
        print("Введен неверный параметр: 'Да / Нет'!")
        return transaction_sorted_by_date(data)


def transaction_filtered_by_currency(data: list[dict]) -> list[dict]:
    """Функция запрашивает о необходимости вывода только рублевых транзакций "Да/Нет".
    При положительном ответе фильтрует данные."""
    currency = input("Выводить только рублевые транзакции? Да/Нет")
    if currency.lower() == "нет":
        return list(data)
    elif currency.lower() == "да":
        return list(filter_by_currency(data, "RUB"))
    else:
        print("Введен неверный параметр: 'Да / Нет'!")
        return transaction_filtered_by_currency(data)


def transaction_filtered_by_description(data: list[dict]) -> list[dict]:
    """Функция запрашивает о необходимости поиска по ключевым словам "Да/Нет"."""
    search_by_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if search_by_description.lower() == "нет":
        return data
    elif search_by_description.lower() == "да":
        search_value = input("Введите слово для поиска.")
        if not search_value:
            print("Слово для поиска не указано!")
            return data
        else:
            return process_bank_search(data, str(search_value))
    else:
        print("Введен неверный параметр: 'Да / Нет'!")
        return transaction_filtered_by_description(data)


def decorator(func: Callable[[], list[dict]]) -> Callable[[], None]:
    """Декоратор, запускает функцию main().
    Выводит приветственное сообщение и транзакции из поиска в формате

    12.11.2019 Перевод с карты на карту
    MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
    Сумма: 130 USD

    18.07.2018 Перевод организации
    Visa Platinum 7492 65** **** 7202 -> Счет **0034
    Сумма: 8390 руб."""
    @wraps(func)
    def wrapper() -> None:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

        searched_data = func()
        if not isinstance(searched_data, list):
            print("Ошибка: функция вернула некорректные данные.")
            return

        print(
            "Распечатываю итоговый список транзакций...\n"
            f"Всего банковских операций в выборке: {len(searched_data)}\n"
        )

        for item in searched_data:
            date = get_date(item.get("date", ""))
            currency = (item.get("operationAmount", {}).get("currency", {}).get("name",  "") or item.get(
                "currency_name", ""
            ))
            amount = (item.get("operationAmount", {}).get("amount", "") or item.get("amount", ""))

            if "from" in item and isinstance(item.get("from"), str):
                sender = mask_account_card(item.get("from", ""))
                recipient = mask_account_card(item.get("to", ""))
                masked_account = f"{sender} -> {recipient}"
            else:
                owner = mask_account_card(item.get("to", ""))
                masked_account = f"{owner}"

            print(f"{date} {item.get("description")}\n{masked_account}\nСумма: {amount} {currency}\n")

    return wrapper


@decorator
def main() -> list[dict]:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""

    data_list = file_type_settings()  # Выбор формата файла и считывание данных.
    sorted_data_by_status = transaction_status(data_list)  # Выбор сортировки по статусу.
    sorted_data_by_date = transaction_sorted_by_date(sorted_data_by_status)  # Сортировка по дате.
    filtered_data_by_currency = transaction_filtered_by_currency(sorted_data_by_date)  # Фильтрация по валюте.
    # Фильтрация по описанию.
    filtered_data_by_description = transaction_filtered_by_description(filtered_data_by_currency)
    return filtered_data_by_description
