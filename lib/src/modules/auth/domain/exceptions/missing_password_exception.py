from lib.src.core.exceptions.http_exception import HttpException


class MissingPasswordException(HttpException):
    def __init__(
        self,
        message="Senha não encontrada no Body",
        code="MISSING_PASSWORD",
        status_code=400,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
