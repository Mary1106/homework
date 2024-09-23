from unittest.mock import patch
from src.external_api import get_transaction_amount_rub


@patch('requests.get')
def test_get_transaction_amount_rub(mocked_get):
    mocked_get.return_value.json.return_value = {
        'success': True,
        'query':
            {
                'from': 'USD',
                'to': 'RUB',
                'amount': 8221.37
            }, 'info':
            {
                'timestamp': 1725983944,
                'rate': 91.347481
            },
        'date': '2024-09-10',
        'result': 751001.439869
    }

    test_transaction = {
        'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount':
            {
                'amount': '8221.37',
                'currency':
                    {
                        'name': 'USD.',
                        'code': 'USD'
                    }
            },
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        'to': 'Счет 64686473678894779589'
    }

    assert get_transaction_amount_rub(test_transaction) == mocked_get.return_value.json.return_value['result']
    mocked_get.assert_called()
