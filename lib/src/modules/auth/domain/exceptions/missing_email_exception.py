from lib.src.core.exceptions.http_exception import HttpException


class MissingEmailException(HttpException):
    def __init__(
        self,
        message="Email não encontrado no Body",
        code="MISSING_EMAIL",
        status_code=400,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
