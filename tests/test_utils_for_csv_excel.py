import pandas as pd
import pytest
import csv
from unittest.mock import patch
from src.utils_for_csv_excel import get_operations_from_csv, get_operations_from_excel


@pytest.fixture
def test_transactions_csv():
    sample_csv = {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 16210.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту"
    }
    return pd.DataFrame(sample_csv)


@pytest.fixture
def test_transactions_excel():
    sample_excel = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }
    return pd.DataFrame(sample_excel)


# @patch('get_operations_from_csv')
# def test_get_operations_from_csv(mock_open, test_transactions_csv):
#     mock_open.return_value.to_dict.return_value = test_transactions_csv
#     result = get_operations_from_csv('C:/users/mary/PycharmProjects/my_prj/homework/data/transactions.csv')
#     expected = test_transactions_csv.to_dict(orient='records')
#     assert result == expected


def test_get_operations_from_csv_with_incorrect_path():
    assert get_operations_from_csv("") == []


# @patch('get_operations_from_excel')
# def test_get_operations_from_excel(mock_pd.read_excel, test_transactions_excel):
#     mock_pd.read_excel.return_value = test_transactions_excel
#     result = get_operations_from_excel('C:/users/mary/PycharmProjects/my_prj/homework/data/transactions.xlsx')
#     expected = test_transactions_excel.to_dict(orient='records')
#     assert result == expected


def test_get_operations_from_excel_with_incorrect_path():
    assert get_operations_from_excel("") == []

