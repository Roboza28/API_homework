# -*- coding: utf-8 -*-
from pandas.errors import EmptyDataError
from requests.exceptions import RequestException, ConnectionError, JSONDecodeError


class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class WrongRequestError(Error):
    pass


class WrongNumSignError(Error):
    pass


class WrongLenListError(Error):
    pass


class WrongLoopBreak(Error):
    pass


def decorator_exceptions(func):
    """ Функция-декоратор для удобной обработки исключений. """
    def wrapper(*args, **kwargs):
        try:
            result_func = func(*args, **kwargs)

        except (WrongRequestError, WrongLenListError, WrongNumSignError) as error1:
            print(f'\nОШИБКА. {error1}')

        except ConnectionError as error2:
            print(f'\nОШИБКА. {error2}')

        except RequestException as error3:
            print(f'\nОШИБКА. Некорректная работа запроса. Код ошибки {error3}')

        except EmptyDataError:
            print(f'\nИстория пуста. Сделайте запрос и повторите команду.')

        except JSONDecodeError:
            print('\nОШИБКА. Невозможно декодировать полученный ответ, повторите запрос.')

        except FileNotFoundError:
            print('\nОШИБКА. Данный файл или каталог отсутствует. Сделайте запрос и повторите команду.')

        except PermissionError:
            print('\nОШИБКА. Вам отказано в доступе к файлу истории или он уже открыт в другом приложении.')

        except KeyboardInterrupt:
            print('\nПринудительное прерывание программы.\nПожалуйста, попробуйте еще раз.')

        except WrongLoopBreak:
            pass

        except Exception as error5:
            print(f'\nОШИБКА. {error5}\nПожалуйста, попробуйте еще раз.')

        else:
            return result_func

    return wrapper
