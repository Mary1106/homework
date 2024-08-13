from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(account_card: str) -> str | None:
    """Принимает на вход тип карты и ее номер или счет и его номер; возвращает маску карты или счета"""
    account_card_splited = account_card.split()
    if len(account_card_splited[-1]) == 16:
        if len(account_card.split()) == 3:
            return f"{account_card_splited[0]} {account_card_splited[1]} {get_mask_card_number(account_card_splited[-1])}"
        else:
            return f"{account_card_splited[0]} {get_mask_card_number(account_card_splited[1])}"
    elif len(account_card_splited[-1]) == 20:
        return f"{account_card_splited[0]} {get_mask_account(account_card_splited[1])}"
    else:
        return None


def get_date(date_time: str) -> str | None:
    """Принимает на вход дату в формате '2024-03-11T02:26:18.671407' и возвращает в формате ДД.ММ.ГГГГ"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[0:4]}"
