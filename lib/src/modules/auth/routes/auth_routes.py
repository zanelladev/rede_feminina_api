from http.client import HTTPException

from flask import Blueprint, Request, jsonify, request

from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.mixins.validate_email_mixin import ValidateEmailMixin
from lib.src.core.mixins.validate_json_body_mixin import ValidateJsonBodyMixin
from lib.src.modules.auth.domain.dtos.sign_in_request_dto import SignInRequestDto
from lib.src.modules.auth.domain.exceptions.invalid_email_exception import (
    InvalidEmailException,
)
from lib.src.modules.auth.domain.exceptions.missing_email_exception import (
    MissingEmailException,
)
from lib.src.modules.auth.domain.exceptions.missing_password_exception import (
    MissingPasswordException,
)
from lib.src.modules.auth.domain.exceptions.user_not_found_exception import (
    UserNotFoundException,
)
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRoutes(ValidateEmailMixin, ValidateJsonBodyMixin):
    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository
        self.blueprint = Blueprint("auth", __name__, url_prefix="/auth")
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule(
            "/signin",
            "signin",
            self.signin,
            methods=["POST"],
        )
        self.blueprint.add_url_rule(
            "/signup",
            "signup",
            self.signup,
            methods=["POST"],
        )
        self.blueprint.add_url_rule(
            "/validate-token",
            "validateToken",
            self.validateToken,
            methods=["POST"],
        )
        self.blueprint.add_url_rule(
            "/refresh-token",
            "refreshToken",
            self.refreshToken,
            methods=["POST"],
        )

    async def signin(self):
        try:
            self._validateJsonRequest(request)

            email = request.json.get("email", None)
            password = request.json.get("password", None)

            self._validateEmailAndPassword(email, password)

            dto = SignInRequestDto(email, password)

            user = await self.auth_repository.signIn(dto)

            await self.auth_repository.refreshToken(user["refreshToken"])

            if user:
                return jsonify(user), 200

            return jsonify(UserNotFoundException().toJson()), 404

        except HTTPException:
            return jsonify(UserNotFoundException().toJson()), 404

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to sign in the user.",
                        "error": str(e),
                    }
                ),
                400,
            )

    async def signup(self):
        try:
            self._validateJsonRequest(request)

            email = request.json.get("email", None)
            password = request.json.get("password", None)

            self._validateEmailAndPassword(email, password)

            await self.auth_repository.signUp()

            return {"msg": "User not found."}, 200

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to sign up the user.",
                        "error": str(e),
                    }
                ),
                400,
            )

    async def validateToken(self):
        try:
            self._validateJsonRequest(request)

            await self.auth_repository.validateToken()

            return {"msg": "User not found."}, 200

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to validate the token.",
                        "error": str(e),
                    }
                ),
                400,
            )

    async def refreshToken(self):
        try:
            self._validateJsonRequest(request)

            await self.auth_repository.refreshToken()

            return {"msg": "User not found."}, 200

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to refresh the token.",
                        "error": str(e),
                    }
                ),
                400,
            )

    def _validateJsonRequest(self, request: Request):
        if not self.validate_json_body(request):
            raise MissingJsonException()

    def _validateEmailAndPassword(self, email: str, password: str):
        if not email:
            raise MissingEmailException()

        if not self.validate_email(email):
            raise InvalidEmailException()

        if not password:
            raise MissingPasswordException()
