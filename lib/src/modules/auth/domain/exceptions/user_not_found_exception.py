from lib.src.core.exceptions.http_exception import HttpException


class UserNotFoundException(HttpException):
    def __init__(
        self,
        message="Usuário não encontrado",
        code="USER_NOT_FOUND",
        status_code=404,
    ):
        super().__init__(message, code, status_code)

    def toJson(self):
        return super().toJson()
