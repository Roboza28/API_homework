from src.interface import show_history, print_current_weather
from src.API import get_city_by_ip, get_weather_from_city
from src.file_management import save_current_weather_to_history, create_clear_csv_file
from src.Exceptions import WrongRequestError, WrongNumSignError, WrongLenListError
from pandas.errors import EmptyDataError
from requests.exceptions import RequestException, ConnectionError, JSONDecodeError


def decorator_exceptions(func):
    """ Функция-декоратор для удобной обработки исключений. """
    def wrapper(*args, **kwargs):
        try:
            result_func = func(*args, **kwargs)
        except WrongRequestError as error1:
            print(f'\nОШИБКА. {error1.message}.')
        except WrongLenListError as error2:
            print(f'\nОШИБКА. {error2.message}.')
        except WrongNumSignError as error3:
            print(f'\nОШИБКА. {error3.message}.')
        except ConnectionError as error4:
            print(f'\nОШИБКА. {error4}.')
        except RequestException as error5:
            print(f'\nОШИБКА. Некорректная работа запроса. Код ошибки {error5}.')
        except EmptyDataError as error6:
            print(f'\nОШИБКА. {error6}')
        except JSONDecodeError:
            print('\nОШИБКА. Невозможно декодировать полученный ответ, повторите запрос.')
        except FileNotFoundError:
            print('\nОШИБКА. Данный файл или каталог отсутствует.')
        except PermissionError:
            print('\nОШИБКА. Вам отказано в доступе к файлу истории или он уже открыт в другом приложении.')
        except KeyboardInterrupt:
            print('\nПринудительное прерывание программы.\nПожалуйста, попробуйте еще раз.')
        except Exception as error7:
            print(f'\nОШИБКА. {error7}.\nПожалуйста, попробуйте еще раз.')
        else:
            return result_func
    return wrapper


@decorator_exceptions
def main() -> None:
    """ Точка входа в программу. """

    print('Добро пожаловать!')
    while True:
        print('\nДоступны следующие команды:\n'
              '1. Получить погоду по Вашему местоположению.\n'
              '2. Получить погоду в городе по названию города.\n'
              '3. Получить историю Ваших запросов.\n'
              '4. Удалить историю запросов.\n'
              '5. Выйти из приложения.')
        match input('\nВыберите номер команды: ').strip():
            case '1':
                city = get_city_by_ip()
                weather_in_city = get_weather_from_city(city)
                print_current_weather(weather_in_city)
                save_current_weather_to_history(weather_in_city)

            case '2':
                city = input('\nВведите город: ').strip()
                weather_in_city = get_weather_from_city(city)
                print_current_weather(weather_in_city)
                save_current_weather_to_history(weather_in_city)

            case '3':
                num_requests = int(input('\nСколько последних запросов Вы хотите увидеть? Введите: ').strip())
                if num_requests < 0:
                    raise WrongNumSignError('\nОшибка. Введено некорректное значение. Введите число больше нуля!')
                show_history(num_requests)

            case '4':
                create_clear_csv_file()
                print('\nИстория очищена.')

            case '5':
                print('\nСпасибо за использование нашего приложения.')
                break

            case _:
                print('\nВведено некорректное значениe. Попробуйте ещё раз.')


if __name__ == '__main__':
    main()
