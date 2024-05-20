from abc import ABC, property, abstractmethod


class BaseException(ABC, Exception):
    _message = None
    _code = None

    @property
    @staticmethod
    def message(self):
        return self._message

    @property
    @staticmethod
    def code(self):
        return self._code

    @abstractmethod
    @staticmethod
    def toJson(self):
        return {
            "message": self.message,
            "code": self.code
        }
