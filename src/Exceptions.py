class WrongRequestError(Exception):
    def __init__(self, message):
        self.message = message


class WrongNumSignError(Exception):
    def __init__(self, message):
        self.message = message


class WrongLenListError(Exception):
    def __init__(self, message):
        self.message = message
