import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return '7000792289606361'


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.fixture
def account():
    return '73654108430135874305'


def test_get_mask_account(account):
    assert get_mask_account(account) == '**4305'
