class MissingPasswordException(BaseException):
    _message = "Missing password"
    _code = "MISSING_PASSWORD"

    def __init__(self):
        super().__init__(self._message, self._code)

    def toJson(self):
        return {
            'message': self._message,
            'code': self._code
        }
