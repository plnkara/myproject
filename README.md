# MyProject

Учебный Python-проект для работы с банковскими операциями: маскировка данных карты и счета, фильтрация операций по статусу, сортировка операций по дате и генераторы для обработки транзакций.

## Реализованные функции

- `get_mask_card_number` маскирует номер банковской карты.
- `get_mask_account` маскирует номер банковского счета.
- `mask_account_card` определяет тип данных и применяет нужную маску.
- `get_date` преобразует дату из ISO-формата в формат `ДД.ММ.ГГГГ`.
- `filter_by_state` возвращает только операции с нужным статусом.
- `sort_by_date` сортирует операции по дате.
- `filter_by_currency` поочередно возвращает транзакции с нужным кодом валюты.
- `transaction_descriptions` поочередно возвращает описания транзакций.
- `card_number_generator` генерирует номера карт в заданном диапазоне.

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

Для установки тестовых и lint-зависимостей:

```bash
poetry install --with test,lint
```

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Запуск тестов с отчётом покрытия:

```bash
poetry run pytest --cov=src --cov-report=html
```

HTML-отчёт покрытия сохраняется в папке `htmlcov/`.
Главная страница отчёта: `htmlcov/index.html`.

## Модуль `generators`

Модуль `src/generators.py` содержит генераторы для ленивой обработки банковских транзакций и генерации номеров карт.

- `filter_by_currency(transactions, currency)` возвращает итератор с транзакциями по коду валюты.
- `transaction_descriptions(transactions)` поочередно возвращает поле `description` из каждой транзакции.
- `card_number_generator(start, stop)` генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

## Пример данных

```python
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
```

```python
transactions = [
    {
        "id": 939719570,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации",
    },
    {
        "id": 873106923,
        "operationAmount": {"currency": {"code": "RUB"}},
        "description": "Перевод со счета на счет",
    },
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

## Примеры использования `filter_by_currency`

```python
from src.generators import filter_by_currency

usd_transactions = list(filter_by_currency(transactions, "USD"))
print(usd_transactions)
```

Результат:

```python
[
    {
        "id": 939719570,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации",
    }
]
```

## Примеры использования `transaction_descriptions`

```python
from src.generators import transaction_descriptions

descriptions = list(transaction_descriptions(transactions))
print(descriptions)
```

Результат:

```python
["Перевод организации", "Перевод со счета на счет"]
```

## Примеры использования `card_number_generator`

```python
from src.generators import card_number_generator

numbers = list(card_number_generator(1, 3))
print(numbers)
```

Результат:

```python
[
    "0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
]
```
