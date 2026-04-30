from collections.abc import Iterator

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    ("currency", "expected_ids"),
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
    ],
)
def test_filter_by_currency_returns_only_matching_transactions(
    transactions: list[dict[str, object]], currency: str, expected_ids: list[int]
) -> None:
    """Проверяет фильтрацию транзакций по коду валюты."""
    result = list(filter_by_currency(transactions, currency))

    assert [transaction["id"] for transaction in result] == expected_ids


def test_filter_by_currency_returns_iterator(transactions: list[dict[str, object]]) -> None:
    """Проверяет, что функция возвращает итератор."""
    result = filter_by_currency(transactions, "USD")

    assert isinstance(result, Iterator)


def test_filter_by_currency_returns_empty_iterator_for_empty_list() -> None:
    """Проверяет работу фильтра с пустым списком транзакций."""
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_stops_with_stop_iteration(transactions: list[dict[str, object]]) -> None:
    """Проверяет корректное завершение генератора фильтрации."""
    result = filter_by_currency(transactions, "RUB")

    assert next(result)["id"] == 873106923
    assert next(result)["id"] == 594226727
    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    ("input_transactions", "expected_descriptions"),
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
        ),
        ([{"description": "Одна транзакция"}], ["Одна транзакция"]),
        ([], []),
    ],
)
def test_transaction_descriptions_returns_descriptions(
    input_transactions: list[dict[str, str]], expected_descriptions: list[str]
) -> None:
    """Проверяет возврат описаний транзакций."""
    assert list(transaction_descriptions(input_transactions)) == expected_descriptions


def test_transaction_descriptions_skips_transactions_without_description(
    transactions: list[dict[str, object]],
) -> None:
    """Проверяет, что транзакции без description не вызывают ошибку."""
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_returns_generator(transactions: list[dict[str, object]]) -> None:
    """Проверяет, что функция возвращает генератор."""
    result = transaction_descriptions(transactions)

    assert isinstance(result, Iterator)


def test_transaction_descriptions_stops_with_stop_iteration() -> None:
    """Проверяет корректное завершение генератора описаний."""
    result = transaction_descriptions([{"description": "Только одна"}])

    assert next(result) == "Только одна"
    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    ("start", "stop", "expected_numbers"),
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (7, 7, ["0000 0000 0000 0007"]),
        (
            9999999999999998,
            9999999999999999,
            ["9999 9999 9999 9998", "9999 9999 9999 9999"],
        ),
    ],
)
def test_card_number_generator_returns_expected_numbers(
    start: int, stop: int, expected_numbers: list[str]
) -> None:
    """Проверяет генерацию и форматирование номеров карт."""
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_handles_min_and_max_values() -> None:
    """Проверяет крайние допустимые значения диапазона."""
    min_value_result = next(card_number_generator(1, 1))
    max_value_result = next(card_number_generator(9999999999999999, 9999999999999999))

    assert min_value_result == "0000 0000 0000 0001"
    assert max_value_result == "9999 9999 9999 9999"


def test_card_number_generator_stops_with_stop_iteration() -> None:
    """Проверяет корректное завершение генератора номеров карт."""
    result = card_number_generator(1, 1)

    assert next(result) == "0000 0000 0000 0001"
    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    ("start", "stop"),
    [
        (0, 5),
        (5, 4),
        (1, 10000000000000000),
    ],
)
def test_card_number_generator_raises_for_invalid_range(start: int, stop: int) -> None:
    """Проверяет ошибку для некорректного диапазона номеров карт."""
    with pytest.raises(ValueError):
        list(card_number_generator(start, stop))
