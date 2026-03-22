import os
from typing import Any

import requests
from dotenv import load_dotenv


def currency_conversion(currency_from: str, currency_to: str = "RUB", amount: int | float = 1) -> float | Any:
    """Функция для обращения к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.
    Для конвертации валюты использован сервис "Exchange Rates Data API": https://apilayer.com/exchangerates_data-api.
    Параметры по умолчанию возвращают курс 1 заданной единицы валюты в рублях.
    """
    load_dotenv()
    API_KEY = os.getenv("API_KEY")


    #    Пример запроса:
    #    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {"amount": amount, "from": currency_from, "to": currency_to}
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=payload)

    status_code = response.status_code
    result = response.json()
    rate = result["info"]["rate"]
    if status_code == 200:
        return rate
    else:
        raise Exception(f"Error {status_code}")