# -*- coding: utf-8 -*-
from src.msg_for_user import MENU, WELCOME, SELECT_COMMAND
from src.service import ACTION_MAP
from src.Exceptions import decorator_exceptions


@decorator_exceptions
def main() -> None:
    """ Точка входа в программу. """
    print(WELCOME)
    while True:
        print(MENU)

        command = input(SELECT_COMMAND).strip()

        action = ACTION_MAP.get(command, None)

        if action:
            action()
        else:
            ACTION_MAP.get(action)()


if __name__ == '__main__':
    main()
