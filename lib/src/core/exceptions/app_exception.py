from abc import ABC, abstractmethod


class AppException(ABC, Exception):
    def __init__(self, message: str, code: str):
        self._message = message
        self._code = code

    @property
    def message(self):
        return self._message

    @property
    def code(self):
        return self._code

    @abstractmethod
    def toJson(self):
        return {"message": self.message, "code": self.code}
