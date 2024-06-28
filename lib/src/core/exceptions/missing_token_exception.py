from lib.src.core.exceptions.http_exception import HttpException


class MissingTokenException(HttpException):
    def __init__(
        self,
        message="Token faltando na requisição",
        code="MISSING_TOKEN",
        status_code=401,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
