import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    ("card_number", "expected_mask"),
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("0123456789012345", "0123 45** **** 2345"),
    ],
)
def test_get_mask_card_number_returns_masked_number(card_number: int | str, expected_mask: str) -> None:
    """Проверяет корректное маскирование номера карты."""
    assert get_mask_card_number(card_number) == expected_mask


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "7000 7922 8960 6361",
        "7000AB2289606361",
        "123456789012345",
        "12345678901234567",
        "",
        None,
    ],
)
def test_get_mask_card_number_raises_for_invalid_data(invalid_card_number: int | str | None) -> None:
    """Проверяет ошибку для некорректного номера карты."""
    with pytest.raises(ValueError):
        get_mask_card_number(str(invalid_card_number) if invalid_card_number is None else invalid_card_number)


@pytest.mark.parametrize(
    ("account_number", "expected_mask"),
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("00000000000000001234", "**1234"),
    ],
)
def test_get_mask_account_returns_masked_number(account_number: int | str, expected_mask: str) -> None:
    """Проверяет корректное маскирование номера счета."""
    assert get_mask_account(account_number) == expected_mask


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "73654108430135AB4305",
        "1234567890123456789",
        "123456789012345678901",
        "",
        None,
    ],
)
def test_get_mask_account_raises_for_invalid_data(invalid_account_number: int | str | None) -> None:
    """Проверяет ошибку для некорректного номера счета."""
    with pytest.raises(ValueError):
        get_mask_account(str(invalid_account_number) if invalid_account_number is None else invalid_account_number)
