import logging


def check(condition: bool, message: str):
    """
    Проверка условия с логированием.
    """
    if condition:
        logging.debug(f"Проверка прошла: {message}")
    else:
        logging.error(f"Проверка не прошла: {message}")
        raise AssertionError(message)


def assert_equal(expected, actual, message=""):
    """
    Проверка на равенство с логированием.
    """
    if expected != actual:
        logging.error(f"{message} | Ожидалось: {expected}, Получено: {actual}")
        raise AssertionError(f"{message} | Ожидалось: {expected}, Получено: {actual}")
    else:
        logging.debug(f"{message} | Значения совпадают: {expected}")
        
def assert_in(substring, string, message=""):
    """
    Проверка на наличие подстроки с логированием.
    """
    if substring not in string:
        logging.error(f"{message} | '{substring}' не найдено в: {string}")
        raise AssertionError(f"{message} | '{substring}' не найдено в: {string}")
    else:
        logging.debug(f"{message} | '{substring}' найдено в строке.")