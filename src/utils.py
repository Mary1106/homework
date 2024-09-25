import json
import os


def get_operations(path_to_json):
    """Принимает на вход путь до JSON-файла; возвращает список словарей из существующего файла с json-данными или
    пустой список, если файл пуст или его нет"""
    if os.path.exists(path_to_json) and os.path.isfile(path_to_json):
        try:
            with open(path_to_json, encoding='utf-8') as f:
                data = json.load(f)
                if type(data) is list:
                    return data
                else:
                    return []
        except Exception:
            return []


# path = "../data/operations.json"
# data = get_operations(path)
# print(data)
