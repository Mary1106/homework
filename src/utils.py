import json
import os
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(path_to_json: str) -> list | None:
    """Принимает на вход путь до JSON-файла; возвращает список словарей из существующего файла с json-данными или
    пустой список, если файл пуст или его нет"""
    if os.path.exists(path_to_json) and os.path.isfile(path_to_json):
        try:
            with open(path_to_json, encoding='utf-8') as f:
                data = json.load(f)
                if type(data) is list:
                    logger.info('Возвращен список словарей из JSON-файла.')
                    return data
                else:
                    logger.info('Возвращен пустой список. JSON-файл пуст или отсутствует.')
                    return []
        except Exception as ex:
            logger.error(f'Возвращен пустой список. Произошла ошибка: {ex}.')
            return []


# path = "../data/operations.json"
# data = get_operations(path)
# print(data)
