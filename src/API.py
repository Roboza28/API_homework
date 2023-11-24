# -*- coding: utf-8 -*-
from settings import USER_UNITS, USER_LANGUAGE, API_KEY, URL
import geocoder
import requests
from http import HTTPStatus
from requests.exceptions import RequestException
from src.Exceptions import decorator_exceptions, WrongRequestError


def get_city_by_ip() -> str:
    """ Функция получает название города по ip.
    Returns:
        str с названием города.
    """
    return geocoder.ip('me').city


def get_request_weather_from_city(request_city: str) -> requests.models.Response:
    """ Функция запрашивает информацию о погоде в требуемом городе.
    После получения ответа от сервера, проверяется статус реквеста.
    В случае успешного реквеста он передается далее для обработки.
    Args:
        request_city: название города.
    Returns:
        requests.models.Response с актуальной погодой.
    """
    params = dict(q=request_city, units=USER_UNITS, lang=USER_LANGUAGE, appid=API_KEY)
    response = requests.get(URL, params=params)
    return response


@decorator_exceptions
def check_request_status(status_code: int) -> bool:
    """ Функция проверяет статус реквеста.
    В случае, если код != 200, вызываются соответствующиеся ошибки с пояснениями.
    Args:
        status_code: статус реквеста.
    """
    if status_code == HTTPStatus.OK:
        return True

    if status_code == HTTPStatus.BAD_REQUEST:
        raise WrongRequestError('\nПустой запрос.')

    if status_code == HTTPStatus.UNAUTHORIZED:
        raise WrongRequestError('\nНеверный API-ключ.')

    if status_code == HTTPStatus.NOT_FOUND:
        raise WrongRequestError('\nТакой город не найден.')

    if status_code > HTTPStatus.INTERNAL_SERVER_ERROR:
        raise WrongRequestError('\nСервер не отвечает. Попробуйте позже.')

    raise RequestException(status_code)
