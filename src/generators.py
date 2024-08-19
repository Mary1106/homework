import random


def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """Функция принимает на список словарей с банковскими операциями и валюту; возвращает список словарей с банковскими
    операициями в указанной валюте"""
    filtered_list = list((x for x in transactions if x["operationAmount"]["currency"]["name"] == currency))
    return filtered_list


def transaction_descriptions(transactions: list[dict]) -> str | None:
    """Генератор принимает на вход список словарей с транзакциями; возвращает описание ("description") каждой
    транзакции по очереди"""
    if len(transactions) == 0:
        return None
    else:
        for i in range(len(transactions)):
            yield transactions[i]["description"]
            i += 1


def card_number_generator(start: int | None = 0, stop: int | None = 9999999999999999) -> str | None:
    """Генератор номера карты, принимает на вход два числа - начало и конец диапазона для генерации номера,
    возвращает номер карты в формате: ХХХХ ХХХХ ХХХХ ХХХХ"""
    if 0 <= start <= 9999999999999999 and 0 <= stop <= 9999999999999999:
        while True:
            random_number = random.randint(start, stop)
            generated_card_number = (16 - len(str(random_number))) * "0" + str(random_number)
            yield (
                f"{generated_card_number[0:4]} {generated_card_number[4:8]} {generated_card_number[8:12]} "
                f"{generated_card_number[12:]}"
            )
    else:
        return None
