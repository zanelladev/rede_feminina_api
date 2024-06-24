from lib.src.core.exceptions.http_exception import HttpException


class InvalidTokenException(HttpException):
    def __init__(
        self,
        message="Token inválido",
        code="INVALID_TOKEN",
        status_code=401,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
