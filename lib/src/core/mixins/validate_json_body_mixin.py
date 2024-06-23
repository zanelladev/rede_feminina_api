from flask import Request


class ValidateJsonBodyMixin:
    @staticmethod
    def validate_json_body(request: Request):
        try:
            if not request.is_json:
                return False

            data = request.get_json()

            if not data:
                return False

            return True

        except Exception:
            return False
