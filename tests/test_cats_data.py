import os.path

from main import Application


# Пример теста, что мы сохранили в файл, но контент файла не проверяется тут никак
def test_facts_saved_to_file(test_application: Application) -> None:
    test_application.save_cat_facts_to_csv(filename="test.csv")

    assert os.path.exists("test.csv")

