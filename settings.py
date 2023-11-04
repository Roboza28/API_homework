from os import getcwd, getenv
from os.path import join

API_KEY = '898f7eab63db25a204def0d3708f8753'
URL = 'https://api.openweathermap.org/data/2.5/weather'

NAME_LOG_FILE = 'history.csv'
USER_LANGUAGE = 'ru'
USER_UNITS = 'metric'
USER_ENCODING = 'windows-1251'
NAME_FOLDER_RESOURCE_PROJECT = 'src'
NAME_FOLDER_LOG_FILES = 'Logs_files'
CURRENT_DIR = getcwd()
PATH_TO_CSV_LOG_FILE = join(CURRENT_DIR, NAME_FOLDER_RESOURCE_PROJECT, NAME_FOLDER_LOG_FILES, NAME_LOG_FILE)
