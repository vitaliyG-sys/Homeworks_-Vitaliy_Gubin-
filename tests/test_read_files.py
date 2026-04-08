from unittest.mock import Mock, patch

import pandas as pd

from src.read_files import read_csv, read_excel


@patch("pandas.read_csv")
def test_open_read_csv(mock_csv_file: Mock, correct_transactions_for_generators: list[dict]) -> None:
    """1. Проверяет работу функции "read_csv" с корректно введенными данными."""
    mock_csv_file.return_value = pd.DataFrame(correct_transactions_for_generators)
    assert read_csv(mock_csv_file) == correct_transactions_for_generators


def test_read_csv_file_not_found() -> None:
    """2. Проверяет работу функции "read_csv" с обработкой ошибки FileNotFoundError."""
    result = read_csv("invalid_path.csv")
    assert isinstance(result, FileNotFoundError)


def test_read_excel(correct_transactions_for_generators: list[dict]) -> None:
    """3. Проверяет работу функции "read_excel" с корректно введенными данными."""
    test_data = pd.DataFrame(correct_transactions_for_generators)

    with patch("pandas.read_excel", return_value=test_data) as mock_read_excel:
        result = read_excel("dummy.xlsx")

        mock_read_excel.assert_called_once_with("dummy.xlsx")
        assert result == correct_transactions_for_generators


def test_read_excel_file_not_found() -> None:
    """4. Проверяет работу функции "read_excel" с обработкой ошибки FileNotFoundError."""
    result = read_excel("invalid_path.csv")
    assert isinstance(result, FileNotFoundError)
