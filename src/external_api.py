import requests
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('API_KEY')


def get_transaction_amount_rub(transaction: dict) -> float | str:
    """Принимает на вход информацию о транзакции в виде словаря; возвращает сумму транзакции в рублях"""
    code = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])
    if code == 'RUB':
        return amount
    else:
        try:
            url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}'
            headers = {'apikey': apikey}
            r = requests.get(url, headers=headers)
            result = r.json()
            return result['result']
        except Exception:
            return 'Error. Please, check transactions data.'

# transaction = {
#     'id': 441945886,
#     'state': 'EXECUTED',
#     'date': '2019-08-26T10:50:58.294041',
#     'operationAmount':
#         {
#             'amount': '8221.37',
#             'currency':
#                 {
#                     'name': 'USD.',
#                     'code': 'USD'
#                 }
#         },
#     'description': 'Перевод организации',
#     'from': 'Maestro 1596837868705199',
#     'to': 'Счет 64686473678894779589'
# }
#
# print(get_transaction_amount_rub(transaction))
