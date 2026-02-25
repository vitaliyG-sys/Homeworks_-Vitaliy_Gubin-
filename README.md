# Homeworks_(Vitaliy_Gubin)

## Описание:

Домашние задания по курсам SkyPro, работа над виджетом банковских операций клиента.

## Установка:

Клонируйте репозиторий:

```
https://github.com/vitaliyG-sys/Homeworks_-Vitaliy_Gubin-.git
```

## Реализованные функции:

### модуль generators.py

1. функция filter_by_currency : Генератор принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).

2. функция transaction_descriptions : Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.

3. функция card_number_generator : Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.

### модуль masks.py

1. функция get_mask_card_number: Принимает номер карты и возвращает в формате 'XXXX XX** **** XXXX'

2. функция get_mask_account: Принимает номер аккаунта и возвращает в формате '**XXXX'

### модуль processing.py

1. функция filter_by_state: Принимает список словарей
   и возвращает список словарей со значением ключа state:"EXECUTED"

2. функция sort_by_date: Принимает список словарей
   и возвращает список словарей отсортированный по дате в порядке убывания

### модуль widget.py

1. функция mask_account_card: Принимает название и номер счета или карты,
   вызывает функцию "get_mask_card_number" или "get_mask_account"
   в зависимости от типа данных и возвращает название с замаскированным номером

2. функция get_date: Принимает строку с датой в формате "2024-03-11T02:26:18.671407"
   и возвращает строку с датой в формате "ДД.ММ.ГГГГ"

## Тестирование:

Тестирование проводится с помощью фреймворка "Pytest".

Для работы необходимо установить Pytest с помощью команды:

```
 poetry add --group dev pytest
 ```

Покрытие тестами составляет 100%

Тесты находятся в пакете "tests"

## Описание тестов:

### модуль tests_masks.py

1. test_get_mask_card_number_correct_value

Проверяет работу функции "get_mask_card_number" с корректно введенными данными.

2. test_get_mask_card_number_incorrect_data

Проверяет работу функции "get_mask_card_number" с неверно введенными данными.

3. test_get_mask_card_number_empty_data

Проверяет работу функции "get_mask_card_number" с пустыми данными.

4. test_get_mask_card_number_incorrect_data_type

Проверяет работу функции "get_mask_card_number" с неправильным типом данных.

5. test_get_mask_account_correct_value

Проверяет работу функции "get_mask_account" с корректно введенными данными.

6. test_get_mask_account_incorrect_data

Проверяет работу функции "get_mask_account" с неверно введенными данными.

7. test_get_mask_account_empty_data

Проверяет работу функции "get_mask_account" с пустыми данными.

8. test_get_mask_account_incorrect_data_type

Проверяет работу функции "get_mask_account" с неправильным типом данных.

### модуль tests_processing.py

1. test_filter_by_state_correct_value

Проверяет работу функции "filter_by_state" с корректно введенными данными

и параметрами  state: "по умолчанию", "EXECUTED" и "CANCELED".

2. test_filter_by_state_incorrect_state

Проверяет работу функции "filter_by_state" с параметром state не указанным в ТЗ.

3. test_filter_by_state_incorrect_data_type_list

Проверяет работу функции "filter_by_state" с неправильным типом данных  'list'.

4. test_filter_by_state_incorrect_data_type_dict

Проверяет работу функции "filter_by_state" с неправильным типом данных  'dict'.

5. test_sort_by_date_correct_value

Проверяет работу функции "sort_by_date" с корректно введенными данными и
    параметрами  order: "по умолчанию", "True" и "False".

6. test_sort_by_date_incorrect_value

Проверяет работу функции "sort_by_date" с некорректными или нестандартными форматами дат.

7. test_sort_by_date_incorrect_data_type_list

Проверяет работу функции "sort_by_date" с неправильным типом данных 'list'.

8. test_sort_by_date_incorrect_data_type_dict

Проверяет работу функции "sort_by_date" с неправильным типом данных 'dict'.

### модуль test_widget.py

1. test_mask_account_card_correct_value

Проверяет работу функции "mask_account_card" с корректно введенными данными.

2. test_mask_account_card_empty_data

Проверяет работу функции "mask_account_card" с пустыми данными.

3. test_mask_account_card_incorrect_value

Проверяет работу функции "mask_account_card" с некорректно введенными данными.

4. test_mask_account_card_incorrect_data_type

Проверяет работу функции "mask_account_card" с неправильным типом данных.

5. test_get_date_correct_value

Проверяет работу функции "get_date" с корректно введенными данными.

6. test_get_date_empty_data

Проверяет работу функции "get_date" с пустыми данными.

7. test_get_date_incorrect_value

Проверяет работу функции "get_date" с некорректно введенными данными.

8. test_get_date_incorrect_data_type

Проверяет работу функции "get_date" с неправильным типом данных.

9. test_get_date_incorrect_calendar_values

Проверяет работу функции "get_date" с неправильными значениями календаря.

### модуль test_generators.py

1. test_filter_by_currency_correct_value

Проверяет работу функции с корректно заданной валютой включая случаи, когда валюта отсутствует.

2. test_filter_by_currency_empty_data

Проверяет работу функции с пустыми данными.

3. test_filter_by_currency_missing_currency

Проверяет работу функции если есть список без соответствующих валютных операций.

4. test_transaction_descriptions_correct_value

Проверяет работу функции с корректно введенными данными и превышением запросов.

5. test_transaction_descriptions_empty_value

Проверяет работу функции с пустым списком.

6. test_card_number_generator_correct_value

Проверяет работу функции на корректность номеров карт в заданном диапазоне
    и корректность форматирования карт.

7. test_card_number_generator_boundary_cases

Проверяет работу функции на соблюдение граничных случаев диапазона номеров карт.