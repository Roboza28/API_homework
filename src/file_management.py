# -*- coding: utf-8 -*-
from settings import PATH_TO_CSV_LOG_FILE, USER_ENCODING
import csv
import pandas as pd
from os import stat
from os.path import isfile


def check_file_for_empty(path_to_file: str) -> bool:
    """ Функция проверяет пустой файл или нет.
    Args:
        path_to_file: путь до файла в виде str.
    Returns:
       Булево значение, принимающее значение True, если файл пустой, и False - в противном случае.
    """
    return stat(path_to_file).st_size == 0


def get_info_from_csv() -> list[dict[str, str]]:
    """ Функция возвращает dataframe с историей всех запросов.
    Returns:
        list, состоящий из словарей, каждый из которых является информацией о погоде.
    """
    if not isfile(PATH_TO_CSV_LOG_FILE):
        create_clear_csv_file()

    if check_file_for_empty(PATH_TO_CSV_LOG_FILE):
        return []

    df_with_history_requests = pd.read_csv(PATH_TO_CSV_LOG_FILE, delimiter=';', encoding=USER_ENCODING)
    history_requests_from_csv = []

    list_col_from_df = df_with_history_requests.columns.values.tolist()
    list_values_from_df = df_with_history_requests.values.tolist()

    for list_value_from_df in list_values_from_df:
        dict_with_request = dict(zip(list_col_from_df, list_value_from_df))
        history_requests_from_csv.append(dict_with_request)

    return history_requests_from_csv


def create_clear_csv_file() -> None:
    """ Функция создает пустой csv файл по указанному в настройках пути. """
    csv_file = open(PATH_TO_CSV_LOG_FILE, 'w+')
    csv_file.close()


def save_current_weather_to_history(current_weather_information: dict) -> None:
    """ Функция получает информацию из лог-файла с предыдущими запросами в виде dataframe.
    Далее добавляет в этот df новый запрос и записывает в csv файл получившийся df.
    Args:
        current_weather_information: словарь с актуальной погодой.
    """
    history_requests_from_csv = get_info_from_csv()
    history_requests_from_csv.append(current_weather_information)

    with open(PATH_TO_CSV_LOG_FILE, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=current_weather_information.keys(), delimiter=';')
        writer.writeheader()
        for request in history_requests_from_csv:
            writer.writerow(request)
