# -*- coding: utf-8 -*-
import datetime
from enum import Enum
from typing import Any
from src.API import get_request_weather_from_city, get_city_by_ip, check_request_status
from src.Exceptions import decorator_exceptions, WrongNumSignError, WrongValueError
from src.printer import print_current_weather, print_history_to_console
from src.storage import save_current_weather_to_history, create_or_clear_csv_file
from src.class_Weather import Weather
from src.msg_for_user import (SELECT_CITY,
                              TEXT_FOR_INT_ERROR,
                              TEXT_FOR_SIGN_ERROR,
                              SELECT_NUM_REQUESTS,
                              TEXT_FOR_ZERO_ERROR,
                              THANK_YOU, CLEAR_HISTORY, NOT_CORRECT_VALUE)


class Command(Enum):
    WEATHER_BY_MYSELF = '1'
    WEATHER_BY_CITY = '2'
    SHOW_HISTORY_REQUESTS_WEATHER = '3'
    CLEAR_HISTORY_REQUESTS_WEATHER = '4'
    EXIT_FROM_PROGRAM = '5'
    NOT_CORRECT_INPUT = None


def adapt_response_time_to_local_time(dict_response: dict[str, Any]) -> datetime:
    """ Функция возвращает актуальное местное время, зависящее от запрашиваемого города.
    Args:
        dict_response: json, преобразованный в словарь.
    Returns:
        datetime с актуальным временем.
    """
    time_seconds = dict_response['dt']
    timedelta_seconds = dict_response['timezone']
    timezone = datetime.timezone(datetime.timedelta(seconds=float(timedelta_seconds)))
    return datetime.datetime.fromtimestamp(float(time_seconds), timezone)


def adapt_response_to_weather(dict_response: dict[str, Any]) -> Weather:
    """ Функция возвращает словарь с данными об актуальной погоде, получая информацию из необработанного словаря.
    Args:
        dict_response: json, преобразованный в словарь.
    Returns:
        dict с актуальной погодой.
    """
    info_about_weather_from_json = Weather(time=adapt_response_time_to_local_time(dict_response),
                                           place=dict_response['name'],
                                           weather=dict_response['weather'][0]['description'],
                                           real_temperature=int(dict_response['main']['temp']),
                                           feels_like_temperature=int(dict_response['main']['feels_like']),
                                           wind_speed=int(dict_response['wind']['speed']))

    return info_about_weather_from_json


def action_weather_by_myself() -> None:
    """ Функция из action map, выполняющая команду №1. """
    city = get_city_by_ip()
    get_weather_from_city(city)


def action_weather_by_city() -> None:
    """ Функция из action map, выполняющая команду №2. """
    city = input(SELECT_CITY).strip()
    get_weather_from_city(city)


def get_weather_from_city(city) -> None:
    """ Функция возвращает погодные условия по названию города.
    Args:
        city: str с названием города.
    """
    request_weather_from_city = get_request_weather_from_city(city)

    if check_request_status(request_weather_from_city.status_code):
        weather_in_city = adapt_response_to_weather(request_weather_from_city.json())
        print_current_weather(weather_in_city.to_dict())
        save_current_weather_to_history(weather_in_city.to_dict())


@decorator_exceptions
def show_history_requests() -> None:
    """ Функция возвращает словарь с данными об актуальной погоде, получая информацию из необработанного словаря."""
    try:
        num_requests = float(input(SELECT_NUM_REQUESTS).strip())
    except ValueError:
        raise WrongValueError('Не удалось преобразовать строку в число. Введите целое неотрицательное число.')

    if num_requests <= 0:
        if num_requests < 0:
            raise WrongNumSignError(TEXT_FOR_SIGN_ERROR)
        else:
            print(TEXT_FOR_ZERO_ERROR)

    if not num_requests.is_integer():
        raise WrongValueError(TEXT_FOR_INT_ERROR)

    print_history_to_console(int(num_requests))


def end_use_program():
    print(THANK_YOU)
    raise StopIteration


def clear_csv():
    create_or_clear_csv_file()
    print(CLEAR_HISTORY)


def not_correct_input():
    print(NOT_CORRECT_VALUE)


ACTION_MAP = {
    Command.WEATHER_BY_MYSELF.value: action_weather_by_myself,
    Command.WEATHER_BY_CITY.value: action_weather_by_city,
    Command.SHOW_HISTORY_REQUESTS_WEATHER.value: show_history_requests,
    Command.CLEAR_HISTORY_REQUESTS_WEATHER.value: clear_csv,
    Command.EXIT_FROM_PROGRAM.value: end_use_program,
    Command.NOT_CORRECT_INPUT.value: not_correct_input
}
