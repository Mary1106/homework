import json
import os

path = "../data/operations.json"

def get_operations(path_to_json):
    """Принимает на вход путь до JSON-файла; возвращает список словарей из существующего файла с json-данными или
    пустой список, если файл пуст или его нет"""
    if os.path.exists(path_to_json) and os.path.isfile(path_to_json):
        try:
            with open(path_to_json, encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception:
            return []

data = get_operations(path)
print(data)






"""Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных 
— float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и 
конвертации суммы операции в рубли. 
Напишите тесты для новых функций, используйте Mock и patch."""