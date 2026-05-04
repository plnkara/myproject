from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(value: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета."""
    parts = value.rsplit(maxsplit=1)
    if len(parts) != 2:
        msg = "Строка должна содержать название и номер."
        raise ValueError(msg)

    name, number = parts

    if name.lower() in {"счет", "счёт"}:
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ из ISO-строки даты и времени."""
    supported_formats = ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d")
    for date_format in supported_formats:
        try:
            parsed_date = datetime.strptime(date_string, date_format)
        except ValueError:
            continue

        return parsed_date.strftime("%d.%m.%Y")

    msg = "Дата должна быть в формате ISO."
    raise ValueError(msg)
