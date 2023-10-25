from os import getcwd, getenv
from os.path import join
from dotenv import load_dotenv


load_dotenv()


API_KEY = getenv('API_KEY')
URL = getenv('URL')
NAME_LOG_FILE = getenv('NAME_LOG_FILE')
USER_LANGUAGE = getenv('USER_LANGUAGE')
USER_UNITS = getenv('USER_UNITS')
USER_ENCODING = getenv('USER_ENCODING')
NAME_FOLDER_RESOURCE_PROJECT = 'src'
NAME_FOLDER_LOG_FILES = 'Logs_files'
CURRENT_DIR = getcwd()
PATH_TO_CSV_LOG_FILE = join(CURRENT_DIR, NAME_FOLDER_RESOURCE_PROJECT, NAME_FOLDER_LOG_FILES, NAME_LOG_FILE)
