# -*- coding: utf-8 -*-
from src.msg_for_user import MENU, WELCOME, CLEAR_HISTORY, THANK_YOU, NOT_CORRECT_VALUE, SELECT_COMMAND
from src.service import Commands, ACTION_MAP
from src.Exceptions import decorator_exceptions


@decorator_exceptions
def main() -> None:
    """ Точка входа в программу. """
    print(WELCOME)
    while True:
        print(MENU)
        match input(SELECT_COMMAND).strip():
            case Commands.WEATHER_BY_MYSELF.value:
                ACTION_MAP[Commands.WEATHER_BY_MYSELF.value]()

            case Commands.WEATHER_BY_CITY.value:
                ACTION_MAP[Commands.WEATHER_BY_CITY.value]()

            case Commands.SHOW_HISTORY_REQUESTS_WEATHER.value:
                ACTION_MAP[Commands.SHOW_HISTORY_REQUESTS_WEATHER.value]()

            case Commands.CLEAR_HISTORY_REQUESTS_WEATHER.value:
                ACTION_MAP[Commands.CLEAR_HISTORY_REQUESTS_WEATHER.value]()
                print(CLEAR_HISTORY)

            case Commands.EXIT_FROM_PROGRAM.value:
                print(THANK_YOU)
                break

            case _:
                print(NOT_CORRECT_VALUE)


if __name__ == '__main__':
    main()
