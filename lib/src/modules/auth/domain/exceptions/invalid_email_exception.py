class InvalidEmailException(BaseException):
    _message = "Invalid email"
    _code = "INVALID_EMAIL"

    def __init__(self):
        super().__init__(self._message, self._code)

    def toJson(self):
        return {"message": self._message, "code": self._code}
