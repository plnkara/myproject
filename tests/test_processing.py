from src.processing import filter_by_state

OPERATIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_uses_default_state() -> None:
    """Проверяет фильтрацию операций со статусом EXECUTED по умолчанию."""
    result = filter_by_state(OPERATIONS)

    assert result == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_filters_by_custom_state() -> None:
    """Проверяет фильтрацию операций по переданному статусу."""
    result = filter_by_state(OPERATIONS, "CANCELED")

    assert result == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_does_not_change_source_list() -> None:
    """Проверяет, что исходный список операций не изменяется."""
    source_operations = OPERATIONS.copy()

    filter_by_state(source_operations)

    assert source_operations == OPERATIONS
