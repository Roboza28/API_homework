from src.Exceptions import WrongRequestError
from settings import USER_UNITS, USER_LANGUAGE, API_KEY, URL
import time
import datetime
import geocoder
import requests
from typing import Any
from http import HTTPStatus
from math import floor
from requests.exceptions import RequestException


def get_city_by_ip() -> str:
    """ Функция получает название города по ip.
    Returns:
        str с названием города.
    """
    return geocoder.ip('me').city


def get_local_time(json_response: [str, Any]) -> datetime:
    """ Функция возвращает актуальное местное время, зависящее от запрашиваемого города.
    Args:
        json_response: json из реквеста.
    Returns:
        datetime с актуальным временем.
    """
    time_seconds = floor(time.time())
    timedelta_seconds = json_response['timezone']
    timezone = datetime.timezone(datetime.timedelta(seconds=float(timedelta_seconds)))
    return datetime.datetime.fromtimestamp(float(time_seconds), timezone)


def parse_info_response(json_response: [str, Any]) -> dict[str, Any]:
    """ Функция возвращает словарь с данными об актуальной погоде, получая информацию из json.
    Args:
        json_response: json-файл из реквеста.
    Returns:
        dict с актуальной погодой.
    """
    info_about_weather_from_json = {'Текущее время': get_local_time(json_response),
                                    'Название города': json_response['name'],
                                    'Погодные условия': json_response['weather'][0]['description'],
                                    'Текущая температура': json_response['main']['temp'],
                                    'Ощущается как': json_response['main']['feels_like'],
                                    'Cкорость ветра': json_response['wind']['speed']
                                    }
    return info_about_weather_from_json


def check_request_status(status_code: int):
    """ Функция проверяет статус реквеста.
    В случае, если код != 200, вызываются соответствующиеся ошибки с пояснениями.
    Args:
        status_code: json-файл из реквеста.
    """
    if status_code == HTTPStatus.OK:
        return
    elif status_code == HTTPStatus.BAD_REQUEST:
        raise WrongRequestError('\nОШИБКА. Пустой запрос.')
    elif status_code == HTTPStatus.UNAUTHORIZED:
        raise WrongRequestError('\nОШИБКА. Неверный API-ключ.')
    elif status_code == HTTPStatus.NOT_FOUND:
        raise WrongRequestError('\nОШИБКА. Такой город/URL не найден.')
    elif status_code > HTTPStatus.INTERNAL_SERVER_ERROR:
        raise WrongRequestError('\nОШИБКА. Сервер не отвечает. Попробуйте позже.')
    else:
        raise RequestException(status_code)


def get_weather_from_city(request_city: str) -> dict:
    """ Функция запрашивает информацию о погоде в требуемом городе.
    После получения ответа от сервера, проверяется статус реквеста.
    В случае успешного реквеста информация парсится и передается далее в виде словаря.
    Args:
        request_city: название города.
    Returns:
        dict с актуальной погодой.
    """
    params = dict(q=request_city, units=USER_UNITS, lang=USER_LANGUAGE, appid=API_KEY)
    response = requests.get(URL, params=params)

    check_request_status(response.status_code)
    weather_from_city = parse_info_response(response.json())
    return weather_from_city
