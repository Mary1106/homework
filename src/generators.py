

def filter_by_currency(transactions: list[dict], currency: str) -> dict | None:
    """Функция принимает на список словарей с банковскими операциями и валюту; возвращает список словарей с банковскими
    операициями в указанной валюте"""
    if len(transactions) == 0:
        return None
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["name"] == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> str | None:
    """Генератор принимает на вход список словарей с транзакциями; возвращает описание ("description") каждой
    транзакции по очереди"""
    if len(transactions) == 0:
        return None
    else:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(start: int = 0, stop: int = 9999999999999999) -> str | None:
    """Генератор номера карты, принимает на вход два числа - начало и конец диапазона для генерации номера,
    возвращает номер карты в формате: ХХХХ ХХХХ ХХХХ ХХХХ"""
    if 0 <= start <= 9999999999999999 and 0 <= stop <= 9999999999999999:
        for n in range(start, stop + 1):
            generated_card_number = (16 - len(str(n))) * "0" + str(n)
            yield (
                f"{generated_card_number[0:4]} {generated_card_number[4:8]} {generated_card_number[8:12]} "
                f"{generated_card_number[12:]}"
            )
    else:
        return None
