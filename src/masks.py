import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Принимает на вход номер карты (7000792289606361) и возвращает его маску (7000 79** **** 6361)."""
    if len(card_number) == 16:
        logger.info('Генерируем маску номера карты.')
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.info('Введен неверный номер карты, маска не сгенерирована.')
        return None


def get_mask_account(account_number: str) -> str | None:
    """Принимает на вход номер счета (73654108430135874305) и возвращает его маску (**4305: ** и последние 4 цифры
    номера)"""
    if len(account_number) == 20:
        logger.info('Генерируем маску номера счета.')
        return f"**{account_number[-4:]}"
    else:
        logger.info('Введен неверный номер счета, маска не сгенерирована.')
        return None

# print(get_mask_card_number('1234567812344568'))
