# -*- coding: utf-8 -*-
from src.file_management import get_info_from_csv_to_list


def print_current_weather(current_weather_information: dict) -> None:
    """ Функция выводит текстовую информацию о погоде, полученную с одного запроса, в консоль.
    Args:
        current_weather_information: словарь с данными о погоде.
    """
    print(f"\nТекущее время: {current_weather_information['Текущее время']}")
    print(f"Название города: {current_weather_information['Название города']}")
    print(f"Погодные условия: {current_weather_information['Погодные условия']}")
    print(f"Текущая температура: {int(current_weather_information['Текущая температура'])} градусов по цельсию")
    print(f"Ощущается как: {int(current_weather_information['Ощущается как'])} градусов по цельсию")
    print(f"Cкорость ветра: {int(current_weather_information['Скорость ветра'])} м/c")


def print_history_to_console(view_num_requests: int) -> None:
    """ Функция выводит в консоль некоторое количество запросов, которые хранятся в csv файле.
    Вывод производится в порядке от нового к старому.
    Если количество запросов, которое запрашивает пользователь, больще, чем находится в лог-файле,
    то будет получена ошибка.
    Args:
        view_num_requests: количество запросов, которые пользователь хочет посмотреть.
    """
    history_requests_from_csv = get_info_from_csv_to_list()

    for request in history_requests_from_csv[:-view_num_requests-1:-1]:
        print_current_weather(request)
