import pandas as pd
import pytest
from unittest.mock import patch
from src.utils_for_csv_excel import get_operations_from_csv, get_operations_from_excel


@pytest.fixture
def test_df():
    """Фикстура, создающая тестовый DataFrame"""
    test_dict = {
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
    return pd.DataFrame(test_dict)


@patch("src.utils_for_csv_excel.pd.read_csv")
def test_get_operations_from_csv(mock_read, test_df):
    mock_read.return_value = test_df
    result = get_operations_from_csv('C:/users/mary/PycharmProjects/my_prj/homework/data/transactions.csv')
    expected = test_df.to_dict(orient='records')
    assert result == expected


def test_get_operations_from_csv_with_incorrect_path():
    assert get_operations_from_csv("") == []


@patch("src.utils_for_csv_excel.pd.read_excel")
def test_get_operations_from_excel(mock_read, test_df):
    mock_read.return_value = test_df
    result = get_operations_from_excel('C:/users/mary/PycharmProjects/my_prj/homework/data/transactions_excel.xlsx')
    expected = test_df.to_dict(orient='records')
    assert result == expected


def test_get_operations_from_excel_with_incorrect_path():
    assert get_operations_from_excel("") == []

