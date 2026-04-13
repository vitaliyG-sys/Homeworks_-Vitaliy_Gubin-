from unittest.mock import Mock, patch

import pytest

from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion_correct_data(mock_get: Mock, correct_transactions_for_generators: list[dict]) -> None:
    """1. Проверяет работу функции "currency_conversion" с корректно введенными данными."""
    apilayer_response = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1773749885, "rate": 81.875366},
        "date": "2026-03-17",
        "result": 81.875366,
    }
    mock_get.return_value.json.return_value = apilayer_response
    mock_get.return_value.status_code = 200
    assert currency_conversion("USD") == 81.875366
    mock_get.assert_called_once()


@patch("requests.get")
def test_currency_conversion_server_error(mock_get: Mock, correct_transactions_for_generators: list[dict]) -> None:
    """2. Проверяет работу функции "currency_conversion" статус-код:500 Internal Server Error."""
    mock_get.return_value.status_code = 500
    with pytest.raises(Exception, match="Error 500"):
        currency_conversion("USD")
