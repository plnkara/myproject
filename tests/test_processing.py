from typing import Any

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date

Operation = dict[str, Any]


@pytest.mark.parametrize(
    ("state", "expected_ids"),
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", [777]),
        ("MISSING", []),
    ],
)
def test_filter_by_state_filters_operations(
    operations: list[Operation], state: str, expected_ids: list[int]
) -> None:
    """Проверяет фильтрацию операций по статусу."""
    result = filter_by_state(operations, state)

    assert [operation["id"] for operation in result] == expected_ids


def test_filter_by_state_uses_default_state(operations: list[Operation]) -> None:
    """Проверяет фильтрацию операций со статусом EXECUTED по умолчанию."""
    result = filter_by_state(operations)

    assert [operation["id"] for operation in result] == [41428829, 939719570]


def test_filter_by_state_returns_empty_list_for_empty_input() -> None:
    """Проверяет работу функции с пустым списком."""
    assert filter_by_state([]) == []


def test_filter_by_state_does_not_change_source_list(operations: list[Operation]) -> None:
    """Проверяет, что исходный список операций не изменяется."""
    source_operations = operations.copy()

    filter_by_state(source_operations)

    assert source_operations == operations


def test_sort_by_date_sorts_descending_by_default(operations: list[Operation]) -> None:
    """Проверяет сортировку операций по дате по убыванию."""
    result = sort_by_date(operations)

    assert [operation["id"] for operation in result] == [778, 777, 41428829, 615064591, 594226727, 939719570]


def test_sort_by_date_sorts_ascending_when_reverse_is_false(operations: list[Operation]) -> None:
    """Проверяет сортировку операций по дате по возрастанию."""
    result = sort_by_date(operations, reverse=False)

    assert [operation["id"] for operation in result] == [939719570, 594226727, 615064591, 41428829, 777, 778]


def test_sort_by_date_keeps_relative_order_for_equal_dates(operations_with_same_dates: list[Operation]) -> None:
    """Проверяет стабильность сортировки при одинаковых датах."""
    result = sort_by_date(operations_with_same_dates)

    assert [operation["id"] for operation in result] == [1, 2, 3]


def test_sort_by_date_sorts_unusual_dates_lexicographically(
    operations_with_unusual_dates: list[Operation],
) -> None:
    """Проверяет поведение сортировки для нестандартных строк дат."""
    result = sort_by_date(operations_with_unusual_dates)

    assert [operation["id"] for operation in result] == [2, 1, 4, 3]


def test_sort_by_date_raises_for_missing_date_key() -> None:
    """Проверяет ошибку, если у операции отсутствует ключ date."""
    operations_without_date = [{"id": 1, "state": "EXECUTED"}]

    with pytest.raises(KeyError):
        sort_by_date(operations_without_date)


def test_sort_by_date_returns_empty_list_for_empty_input() -> None:
    """Проверяет работу сортировки с пустым списком."""
    assert sort_by_date([]) == []


def test_sort_by_date_does_not_change_source_list(operations: list[Operation]) -> None:
    """Проверяет, что сортировка не изменяет исходный список операций."""
    source_operations = operations.copy()

    sort_by_date(source_operations)

    assert source_operations == operations
