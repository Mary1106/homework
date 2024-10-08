import os
import datetime
from utils import get_operations
from utils_for_csv_excel import get_operations_from_csv, get_operations_from_excel
from processing import filter_by_state, sort_by_date
from search import search
from widget import mask_account_card, get_date


path_to_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
path_to_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.csv')
path_to_excel = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions_excel.xlsx')


def main():
    """Функция, которая выводит список словарей с транзакциями пользователя, отбирая их по заданным критериям."""

    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    while True:
        input_file_type = input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла

    """)
    # ШАГ 1: Получаем transactions - список словарей со всеми транзакциями из файла, выбранного пользователем:
        if input_file_type == '1':
            print('Для обработки выбран JSON-файл.')
            transactions = get_operations(path_to_json)
            break
        elif input_file_type == '2':
            print('Для обработки выбран CSV-файл.')
            transactions = get_operations_from_csv(path_to_csv)
            break
        elif input_file_type == '3':
            print('Для обработки выбран XLSX-файл.')
            transactions = get_operations_from_excel(path_to_excel)
            break
        else:
            print(f'Невозможно получить информацию.')

    # ШАГ 2: Фильтруем список словарей по статусу ('state'), выбранному пользователем, и получаем новый список
    # словарей second_step_transactions:
    while True:
        input_status = input("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
        """)
        status_list = ['EXECUTED', 'CANCELED', 'PENDING']
        if input_status.upper() not in status_list:
            print(f'Статус операции {input_status} недоступен.')
        else:
            print(f'Операции отфильтрованы по статусу {input_status.upper()}')
            break

    second_step_transactions = filter_by_state(transactions, state=input_status.upper())

    # ШАГ 3: Сортируем или не сортируем операции по дате (по возрастанию или по убыванию) и получаем новый список
    # словарей third_step_transactions:
    input_sort = input("""Отсортировать операции по дате? Да/Нет 
    """)
    if input_sort.upper() == 'ДА':
        input_sort_type = input("""Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
            """)
        if input_sort_type.upper() == 'ПО ВОЗРАСТАНИЮ':
            third_step_transactions = sort_by_date(second_step_transactions, reverse=False)
        elif input_sort_type.upper() == 'ПО УБЫВАНИЮ':
            third_step_transactions = sort_by_date(second_step_transactions)
        else:
            third_step_transactions = second_step_transactions
    else:
        third_step_transactions = second_step_transactions

    # ШАГ 4: Фильтруем операции по валюте - только рублевые ли все, получаем новый список
    # словарей fourth_step_transactions:
    input_rub_only = input("""Выводить только рублевые транзакции? Да/Нет
        """)
    if input_rub_only.upper() == 'ДА':
        fourth_step_transactions = []
        for transaction in third_step_transactions:
            if transaction['operationAmount']['currency']['code'] == 'RUB':
                fourth_step_transactions.append(transaction)
            else:
                continue
    else:
        fourth_step_transactions = third_step_transactions

    # ШАГ 5: Фильтруем операции по поиску строки в поле description или не фильтруем, получаем новый список
    # словарей fifth_step_transactions:
    input_filter = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет
    """)
    if input_filter.upper() == 'ДА':
        input_for_filter = input("""Введите слово для фильтрации списка транзакций:
        """)
        fifth_step_transactions = search(fourth_step_transactions, input_for_filter)
    else:
        fifth_step_transactions = fourth_step_transactions

    print('Распечатываю итоговый список транзакций...')

    operations_count = len(fifth_step_transactions)
    if operations_count > 0:
        print(f'Всего банковских операций в выборке: {operations_count}')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    for transaction in fifth_step_transactions:
        date = get_date(transaction['date'])
        description = transaction['description']
        if 'from' in transaction.keys():
            masked_data = f"{mask_account_card(transaction['from'])} -> " + f"{mask_account_card(transaction['to'])}"
        else:
            masked_data = f"{mask_account_card(transaction['to'])}"
        amount = f'{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}'
        print(f'{date} {description} \n{masked_data}\nСумма: {amount}\n')



main()

# 08.12.2019 Открытие вклада
# Счет **4321
# Сумма: 40542 руб.
#
# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
#
# 18.07.2018 Перевод организации
# Visa Platinum 7492 65** **** 7202 -> Счет **0034
# Сумма: 8390 руб.
#
# 03.06.2018 Перевод со счета на счет
# Счет **2935 -> Счет **4321
# Сумма: 8200 EUR
