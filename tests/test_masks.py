from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_account() -> None:
    assert get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_card_number_raises_for_non_digits() -> None:
    try:
        get_mask_card_number("7000AB2289606361")
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидался ValueError для номера карты с нецифровыми символами.")


def test_get_mask_account_raises_for_non_digits() -> None:
    try:
        get_mask_account("73654108430135AB4305")
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидался ValueError для номера счета с нецифровыми символами.")
