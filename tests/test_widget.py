import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
    ],
)
def test_mask_account_card_returns_masked_value(value: str, expected_result: str) -> None:
    """Проверяет маскирование карт и счетов."""
    assert mask_account_card(value) == expected_result


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        "AccountWithoutNumber",
        "Visa 1234",
        "Mastercard 1234ABCD5678EFGH",
    ],
)
def test_mask_account_card_raises_for_invalid_data(invalid_value: str) -> None:
    """Проверяет ошибку для некорректной строки карты или счета."""
    with pytest.raises(ValueError):
        mask_account_card(invalid_value)


@pytest.mark.parametrize(
    ("date_string", "expected_result"),
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2024-3-1", "01.03.2024"),
    ],
)
def test_get_date_returns_formatted_date(date_string: str, expected_result: str) -> None:
    """Проверяет преобразование даты в строку формата ДД.ММ.ГГГГ."""
    assert get_date(date_string) == expected_result


@pytest.mark.parametrize(
    "invalid_date_string",
    [
        "",
        "2024/03/11",
        "not-a-date",
        "2024-13-40T00:00:00",
    ],
)
def test_get_date_raises_for_invalid_format(invalid_date_string: str) -> None:
    """Проверяет ошибку для строк без ожидаемого формата даты."""
    with pytest.raises(ValueError):
        get_date(invalid_date_string)
