from lib.src.core.exceptions.http_exception import HttpException


class MissingJsonException(HttpException):
    def __init__(
        self,
        message="JSON body não encontrado na requisição",
        code="MISSING_JSON",
        status_code=400,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
