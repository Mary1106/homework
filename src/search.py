import re


def search(transactions: list[dict], pattern: str) -> list[dict] | None:
    """Функция, которая принимает на вход список словарей с транзакциями и строку для поиска; возвращает список
    словарей, в которых в значение по ключу 'description' содержит заданную для поиска строку."""
    filtered_by_search_transactions = []
    for transaction in transactions:
        if 'description' in transaction.keys():
            if re.search(pattern, transaction['description'], flags=re.IGNORECASE):
                filtered_by_search_transactions.append(transaction)
            else:
                continue
        else:
            continue
    return filtered_by_search_transactions
