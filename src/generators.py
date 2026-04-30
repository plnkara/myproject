from collections.abc import Generator
from collections.abc import Iterator
from typing import Any

Transaction = dict[str, Any]


def filter_by_currency(transactions: list[Transaction], currency: str) -> Iterator[Transaction]:
    """Поочередно возвращает транзакции с указанным кодом валюты."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")
        if not isinstance(operation_amount, dict):
            continue

        currency_info = operation_amount.get("currency")
        if not isinstance(currency_info, dict):
            continue

        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[Transaction]) -> Generator[str, None, None]:
    """Поочередно возвращает описания транзакций."""
    for transaction in transactions:
        description = transaction.get("description")
        if isinstance(description, str):
            yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в указанном диапазоне."""
    min_value = 1
    max_value = 9999999999999999

    if start < min_value or stop > max_value or start > stop:
        msg = "Диапазон номеров карт должен быть от 1 до 9999999999999999."
        raise ValueError(msg)

    for number in range(start, stop + 1):
        number_str = f"{number:016d}"
        yield f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
