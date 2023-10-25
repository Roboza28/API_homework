# -*- coding: utf-8 -*-
from src.file_management import get_info_from_csv
from src.Exceptions import WrongLenListError


def print_current_weather(current_weather_information: dict) -> None:
    """ Функция выводит текстовую информацию о погоде, полученную с одного запроса, в консоль.
    Args:
        current_weather_information: словарь с данными о погоде.
    """
    print(f"\nТекущее время: {current_weather_information['Текущее время']}")
    print(f"Название города: {current_weather_information['Название города']}")
    print(f"Погодные условия: {current_weather_information['Погодные условия']}")
    print(f"Текущая температура: {float(current_weather_information['Текущая температура']):.0f} градусов по цельсию")
    print(f"Ощущается как: {float(current_weather_information['Ощущается как']):.0f} градусов по цельсию")
    print(f"Cкорость ветра: {float(current_weather_information['Cкорость ветра']):.0f} м/c")


def show_history(view_num_requests: int) -> None:
    """ Функция выводит в консоль некоторое количество запросов, которые хранятся в csv файле.
    Вывод производится в порядке от нового к старому.
    Если количество запросов, которое запрашивает пользователь, больще, чем находится в лог-файле,
    то будет получена ошибка.
    Args:
        view_num_requests: количество запросов, которые пользователь хочет посмотреть.
    """
    history_requests_from_csv = get_info_from_csv()

    if view_num_requests > len(history_requests_from_csv):
        raise WrongLenListError(f'\nОШИБКА. Длина истории запросов ({len(history_requests_from_csv):}) меньше, '
                                f'чем указанное число ({view_num_requests}).')
    else:
        for request in history_requests_from_csv[:-view_num_requests-1:-1]:
            print_current_weather(request)
