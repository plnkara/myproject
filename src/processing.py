from typing import Any

Operation = dict[str, Any]


def filter_by_state(operations: list[Operation], state: str = "EXECUTED") -> list[Operation]:
    """Возвращает новый список операций с указанным статусом."""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[Operation], reverse: bool = True) -> list[Operation]:
    """Возвращает новый список операций, отсортированный по дате."""
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
