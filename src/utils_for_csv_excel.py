import pandas as pd
import csv
import os


def get_operations_from_csv(path_to_csv: str) -> list:
    """Принимает на вход путь до CSV-файла; возвращает список словарей из существующего файла с csv-данными или
        пустой список, если файл пуст или его нет"""
    if os.path.exists(path_to_csv) and os.path.isfile(path_to_csv):
        try:
            df = pd.read_csv(path_to_csv, delimiter=';')
            result = df.to_dict(orient='records')
            return result
        except Exception:
            return []
    else:
        return []


def get_operations_from_excel(path_to_excel: str) -> list:
    """Принимает на вход путь до Excel-файла; возвращает список словарей из существующего файла с excel-данными или
        пустой список, если файл пуст или его нет"""
    if os.path.exists(path_to_excel) and os.path.isfile(path_to_excel):
        try:
            df = pd.read_excel(path_to_excel)
            result = df.to_dict(orient='records')
            return result
        except Exception:
            return []
    else:
        return []
