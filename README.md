# Установка зависимостей

## Создание виртуального окружения

```bash
python -m venv .venv
```

## Активация виртуального окружения

```bash
source .venv/bin/activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```


## Как запустить:

В Pycharm запустить файлик `main.py`


Или из консоли командой из корня приложения

```bash
python3 main.py
```

## Задание:

Написать тесты на `pytest` и `requests`, которые проверяют следующий функционал:

- Мы открыли api https://catfact.ninja/facts
- Нашли все факты о котах
- Записали это в файл `data/cats_cats.csv`

Методы которые надо проверить:

- `save_cat_facts_to_csv` что данные с сайта https://catfact.ninja/facts действительно сохранились в csv файлик в папку `tests/test.csv`
- `get_cats_facts_from_web` что возвращает непустой список данных (```python len(test_application.get_cats_facts_from_web) != 0```))
- `load_cat_facts_from_csv` что возвращает непустой список строк