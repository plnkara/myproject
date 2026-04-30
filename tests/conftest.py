from typing import Any

import pytest

Operation = dict[str, Any]


@pytest.fixture
def operations() -> list[Operation]:
    """Возвращает набор операций с разными статусами для тестов."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 777, "state": "PENDING", "date": "2020-01-01T00:00:00.000000"},
        {"id": 778, "date": "2020-02-01T00:00:00.000000"},
    ]


@pytest.fixture
def operations_with_same_dates() -> list[Operation]:
    """Возвращает операции с одинаковыми датами для проверки стабильной сортировки."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-31T23:59:59.000000"},
    ]


@pytest.fixture
def operations_with_unusual_dates() -> list[Operation]:
    """Возвращает операции с нестандартными датами для проверки лексикографической сортировки."""
    return [
        {"id": 1, "date": "2024-01-02"},
        {"id": 2, "date": "bad-date"},
        {"id": 3, "date": "2023-12-31"},
        {"id": 4, "date": "2024-01-02"},
    ]
