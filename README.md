# MyProject

Учебный Python-проект для работы с банковскими операциями: маскировка данных карты и счета, фильтрация операций по статусу и сортировка операций по дате.

## Реализованные функции

- `get_mask_card_number` маскирует номер банковской карты.
- `get_mask_account` маскирует номер банковского счета.
- `mask_account_card` определяет тип данных и применяет нужную маску.
- `get_date` преобразует дату из ISO-формата в формат `ДД.ММ.ГГГГ`.
- `filter_by_state` возвращает только операции с нужным статусом.
- `sort_by_date` сортирует операции по дате.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/plnkara/myproject.git
cd myproject
```

2. Установите зависимости через Poetry:

```bash
poetry install
```

3. Активируйте виртуальное окружение Poetry:

```bash
poetry shell
```

## Пример данных

```python
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
```

## Примеры использования `filter_by_state`

```python
from src.processing import filter_by_state

executed_operations = filter_by_state(operations)
print(executed_operations)
```

Результат:

```python
[
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
```

```python
canceled_operations = filter_by_state(operations, state="CANCELED")
print(canceled_operations)
```

Результат:

```python
[
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
```

## Примеры использования `sort_by_date`

```python
from src.processing import sort_by_date

sorted_operations_desc = sort_by_date(operations)
print(sorted_operations_desc)
```

Результат:

```python
[
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
```

```python
sorted_operations_asc = sort_by_date(operations, reverse=False)
print(sorted_operations_asc)
```

Результат:

```python
[
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]
```
