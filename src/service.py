# -*- coding: utf-8 -*-
import datetime
from enum import Enum
from typing import Any
from src.API import get_request_weather_from_city, get_city_by_ip, check_request_status
from src.Exceptions import decorator_exceptions, WrongNumSignError
from src.interface import print_current_weather, print_history_to_console
from src.file_management import save_current_weather_to_history, create_or_clear_csv_file
from src.msg_for_user import SELECT_CITY, TEXT_FOR_NUM_ERROR, TEXT_FOR_SIGN_ERROR, SELECT_NUM_REQUESTS
from src.class_Weather import Weather


class Commands(Enum):
    WEATHER_BY_MYSELF = '1'
    WEATHER_BY_CITY = '2'
    SHOW_HISTORY_REQUESTS_WEATHER = '3'
    CLEAR_HISTORY_REQUESTS_WEATHER = '4'
    EXIT_FROM_PROGRAM = '5'


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
    city = get_city_by_ip()
    get_weather_from_city(city)


def action_weather_by_city() -> None:
    city = input(SELECT_CITY).strip()
    get_weather_from_city(city)


def get_weather_from_city(city) -> None:
    request_weather_from_city = get_request_weather_from_city(city)

    if check_request_status(request_weather_from_city.status_code):

        weather_in_city = adapt_response_to_weather(request_weather_from_city.json())

        print_current_weather(weather_in_city.info_to_dict())
        # print(weather_in_city)
        save_current_weather_to_history(weather_in_city.info_to_dict())


@decorator_exceptions
def show_history_requests() -> None:
    num_requests = float(input(SELECT_NUM_REQUESTS).strip())

    if num_requests < 0:
        raise WrongNumSignError(TEXT_FOR_SIGN_ERROR)

    if not num_requests.is_integer():
        raise WrongNumSignError(TEXT_FOR_NUM_ERROR)

    print_history_to_console(int(num_requests))


ACTION_MAP = {
    Commands.WEATHER_BY_MYSELF.value: action_weather_by_myself,
    Commands.WEATHER_BY_CITY.value: action_weather_by_city,
    Commands.SHOW_HISTORY_REQUESTS_WEATHER.value: show_history_requests,
    Commands.CLEAR_HISTORY_REQUESTS_WEATHER.value: create_or_clear_csv_file
}
