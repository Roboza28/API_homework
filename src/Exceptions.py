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

        except (WrongRequestError, WrongLenListError, WrongNumSignError) as custom_err:
            print(f'\nОШИБКА. {custom_err}')

        except ConnectionError as connect_err:
            print(f'\nОШИБКА. {connect_err}')

        except RequestException as req_err:
            print(f'\nОШИБКА. Некорректная работа запроса. Код ошибки {req_err}')

        except EmptyDataError:
            print(f'\nИстория пуста. Сделайте запрос и повторите команду.')

        except JSONDecodeError:
            print('\nОШИБКА. Невозможно декодировать полученный ответ, повторите запрос.')

        except ValueError:
            print('\nОШИБКА. Не удалось преобразовать строку в число. Введите целое неотрицательное число.')

        except FileNotFoundError:
            print('\nОШИБКА. Данный файл или каталог отсутствует. Сделайте запрос и повторите команду.')

        except PermissionError:
            print('\nОШИБКА. Вам отказано в доступе к файлу истории или он уже открыт в другом приложении.')

        except KeyboardInterrupt:
            print('\nПринудительное прерывание программы.\nПожалуйста, попробуйте еще раз.')

        except WrongLoopBreak:
            pass

        except Exception as exception:
            print(f'\nОШИБКА. {exception}\nПожалуйста, попробуйте еще раз.')

        else:
            return result_func

    return wrapper
