import pandas as pd


def read_csv(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV. Возвращает список словарей с транзакциями."""
    try:
        with open(path, "r", newline="", encoding="utf-8") as csv_file:
            df = pd.read_csv(csv_file, delimiter=";")
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        return []


def read_excel(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel. Возвращает список словарей с транзакциями."""
    try:
        df = pd.read_excel(path)
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        return []
