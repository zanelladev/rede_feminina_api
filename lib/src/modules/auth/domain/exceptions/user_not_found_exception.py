class UserNotFoundException(BaseException):
    _message = "User not found"
    _code = "USER_NOT_FOUND"

    def __init__(self):
        super().__init__(self._message, self._code)

    def toJson(self):
        return {"message": self._message, "code": self._code}
