from flask import Request


class MissingJsonException(BaseException):
    _message = "Missing JSON in request"
    _code = "MISSING_JSON"

    def __init__(self):
        super().__init__(self._message, self._code)

    def toJson(self):
        return {
            'message': self._message,
            'code': self._code
        }

    @staticmethod
    def validate_request(request: Request):
        try:
            if not request.is_json:
                return False

            data = request.get_json()

            if not data:
                return False

            return True

        except Exception:
            return False
