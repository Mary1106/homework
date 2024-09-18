# Серверная часть виджета банковских операций

Отображает операции клиента.

**Умеет:**

- отображать маски номеров карт и счетов, 
- отображать операции в хронологическом порядке,
- отображать операции по статусу
- генерировать номер карты
- фильтровать операции по валюте
- отображать описание транзакций 
- сохранять логи


## Установка и использование
1. Клонируйте репозиторий:
```
git clone https://github.com/Mary1106/homework/.git
```
2. Установите зависимости:
```
poetry add requests
```
3. 

## Использование
1. ...
2. ...
3. ...

## Примеры использования
#### 1. Функция get_mask_card_number
Принимает на вход номер карты:

```get_mask_card_number(card_number)```

Возвращает его маску.

**Пример входных данных:**

 ```'7000792289606361' ```

**Выход функции:**

```'7000 79** **** 6361'```

#### 2. Функция get_mask_account
Принимает на вход номер счета:

```get_mask_account(account_number)```

Возвращает его маску.

**Пример входных данных:**

 ```'73654108430135874305' ```

**Выход функции:**

```'**4305'```


#### 3. Функция mask_account_card
Принимает на вход тип карты и ее номер или счет и его номер:

```mask_account_card(account_card)```

Возвращает маску карты или счета.

**Пример входных данных:**

Карта: ```'Visa Platinum 7000792289606361'```

Счет:```'Счет 73654108430135874305'```

**Выход функции:**

Карта:```'Visa Platinum 7000 79** **** 6361'```

Счет:```'Счет **4305'```


#### 4. Функция get_date

Принимает на вход дату в формате '2024-03-11T02:26:18.671407':

```get_date(date_time)```

Возвращает дату в формате ДД.ММ.ГГГГ.

**Пример входных данных:**

```'2024-03-11T02:26:18.671407'```

**Выход функции:**

```'11.03.2024'```


#### 5. Функция filter_by_state
Принимает на вход список словарей и ключ:

```filter_by_state(list_of_dict, state="EXECUTED")```

Возвращает список словарей, в которых ключ совпадает с указанным, либо, если ключ не указан, список словарей 
со значением ```state``` по умолчанию: ```'EXECUTED'```.

**Пример входных данных:**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

**Выход функции со статусом по умолчанию 'EXECUTED'**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

**Выход функции, если вторым аргументом передано 'CANCELED'**

```
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
#### 6. Функция sort_by_date
Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание):

```
sort_by_date(list_of_dict, reverse=True)
```

Возвращает отсортированный список словарей.

**Пример входных данных для проверки функции**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

**Выход функции, если порядок сортировки не указан (т.е. по убыванию)**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

## Тестирование
Для проекта реализованы юнит-тесты на pytest. 
Команда для запуска:
```pytest .```
### Покрытие:
```
src\masks.py ........ 100%
src\widget.py ....... 100%
src\processing.py ... 100%
src\widget.py ....... 100%
```
## Документация и ссылки
## Лицензия
Проект распространяется под [лицензией MIT](LICENSE).