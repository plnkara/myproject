from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(value: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета."""
    name, number = value.rsplit(maxsplit=1)

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ из ISO-строки даты и времени."""
    date_part = date_string[:10]
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
