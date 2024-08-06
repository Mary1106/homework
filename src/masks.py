def get_mask_card_number(card_number: str) -> str | None:
    """Принимает на вход номер карты (7000792289606361) и возвращает его маску (7000 79** **** 6361)."""
    if len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    """Принимает на вход номер счета (73654108430135874305) и возвращает его маску (**4305: ** и последние 4 цифры
    номера)"""
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return None
