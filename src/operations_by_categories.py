import pandas as pd


def operations_by_category(transactions) -> dict | None:
    """Функция принимает на вход список словарей с транзакциями; возвращает словарь, где ключи - это типы операций
    ('description'), значения - количество операций данного типа."""
    df = pd.DataFrame(transactions)
    result = df.groupby('description')['id'].count()
    return result.to_dict()
