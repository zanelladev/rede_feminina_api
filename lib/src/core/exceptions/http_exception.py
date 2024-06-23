from lib.src.core.exceptions.app_exception import AppException


class HttpException(AppException):
    """Classe base abstrata para exceções HTTP personalizadas.

    Args:
        message (str): A mensagem de erro.
        code (str): O código de erro.
        status_code (int): O código de status HTTP.
    """

    def __init__(self, message: str, code: str, status_code: int):
        self._message = message
        self._code = code
        self._status_code = status_code

    @property
    def message(self):
        """str: A mensagem de erro."""
        return self._message

    @property
    def code(self):
        """str: O código de erro."""
        return self._code

    @property
    def status_code(self):
        """int: O código de status HTTP."""
        return self._status_code

    def toJson(self):
        """Retorna uma representação JSON da exceção.

        Returns:
            dict: Um dicionário contendo a mensagem de erro, o código de erro e o código de status HTTP.
        """
        return {
            "message": self.message,
            "code": self.code,
        }
