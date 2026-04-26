from typing import Any

Operation = dict[str, Any]


def filter_by_state(operations: list[Operation], state: str = "EXECUTED") -> list[Operation]:
    """Возвращает новый список операций с указанным статусом."""
    return [operation for operation in operations if operation.get("state") == state]
