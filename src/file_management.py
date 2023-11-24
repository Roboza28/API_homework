# -*- coding: utf-8 -*-
from settings import PATH_TO_CSV_LOG_FILE, USER_ENCODING
import csv
import pandas as pd
from os import stat
from os.path import isfile


def report_to_storage() -> pd.DataFrame:
    """ Функция обращается к хранилищу. Если хранилища нет, то создает его.
    После проверки, возвращает dataframe с историей всех запросов.
    Returns:
       DataFrame с историей всех запросов.
    """
    if not isfile(PATH_TO_CSV_LOG_FILE):
        create_or_clear_csv_file()
    return pd.read_csv(PATH_TO_CSV_LOG_FILE, delimiter=';', encoding=USER_ENCODING)


def get_info_from_csv_to_list() -> list[dict[str, str]]:
    """ Функция возвращает историю всех запросов в виде list.
    Returns:
        list, состоящий из словарей, каждый из которых является реквестом.
    """
    history_requests_from_csv = report_to_storage()

    list_col_from_df = history_requests_from_csv.columns.values.tolist()
    list_values_from_df = history_requests_from_csv.values.tolist()

    history_requests = [dict(zip(list_col_from_df, list_value_from_df)) for list_value_from_df in list_values_from_df]

    return history_requests


def check_file_for_empty(path_to_file: str) -> bool:
    """ Функция проверяет пустой файл или нет.
    Args:
        path_to_file: путь до файла в виде str.
    Returns:
       Булево значение, принимающее значение True, если файл пустой, и False - в противном случае.
    """
    return stat(path_to_file).st_size == 0


def create_or_clear_csv_file() -> None:
    """ Функция создает пустой csv файл по указанному в настройках пути. """
    with open(PATH_TO_CSV_LOG_FILE, 'w+'):
        pass


def save_current_weather_to_history(current_weather_information: dict) -> None:
    """ Функция получает информацию из лог-файла с предыдущими запросами в виде dataframe.
    Далее добавляет в этот df новый запрос и записывает в csv файл получившийся df.
    Args:
        current_weather_information: словарь с актуальной погодой.
    """
    field_names_in_csv = current_weather_information.keys()

    with open(PATH_TO_CSV_LOG_FILE, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names_in_csv, delimiter=';')
        if check_file_for_empty(PATH_TO_CSV_LOG_FILE):
            writer.writeheader()
        writer.writerow(current_weather_information)
