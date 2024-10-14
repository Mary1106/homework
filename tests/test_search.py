import pytest
from src.search import search


@pytest.fixture
def example_transactions():
    return [
        {
            'id': 41428829,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364',
            'operationAmount':
                {
                    'amount': '8221.37',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'MasterCard 7158300734726758',
            'to': 'Счет 35383033474447895560'
        },
        {
            'id': 939719570,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount':
                {
                    'amount': '9824.07',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
        },
        {
            'id': 587085106,
            'state': 'EXECUTED',
            'date': '2018-03-23T10:45:06.972075',
            'operationAmount':
                {
                    'amount': '48223.05',
                    'currency':
                        {
                            'name': 'руб.',
                            'code': 'RUB'
                        }
                },
            'description': 'Открытие вклада',
            'to': 'Счет 41421565395219882431'
        }
    ]


def test_search(example_transactions):
    assert search(example_transactions, 'перевод') == [
        {
            'id': 41428829,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364',
            'operationAmount':
                {
                    'amount': '8221.37',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'MasterCard 7158300734726758',
            'to': 'Счет 35383033474447895560'
        },
        {
            'id': 939719570,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount':
                {
                    'amount': '9824.07',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
        },
        ]


def test_search_without_pattern(example_transactions):
    assert search(example_transactions, '') == example_transactions


def test_search_with_bad_pattern(example_transactions):
    assert search(example_transactions, 'abcd') == []