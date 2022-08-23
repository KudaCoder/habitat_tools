import json


class HabitatException(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message

    def json(self):
        return {"error": self.message}


class ConnectionException(HabitatException):
    pass


class DataException(HabitatException):
    pass


class RequestException(HabitatException):
    pass


class ResponseException(HabitatException):
    pass
