from http.client import HTTPException

from flask import Blueprint, Request, jsonify, request

from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.mixins.validate_email_mixin import ValidateEmailMixin
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


class AuthRoutes(ValidateEmailMixin):
    auth_repository = None

    blueprint = Blueprint("auth", __name__, url_prefix="/auth")

    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository

    @blueprint.route("/signin", methods=["POST"])
    async def signin(self):
        try:
            AuthRoutes._validateJsonRequest(request)

            email = request.json.get("email", None)
            password = request.json.get("password", None)

            AuthRoutes._validateEmailAndPassword(email, password)

            dto = SignInRequestDto(email, password)

            user = await self.auth_repository.signIn(dto)

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

    @blueprint.route("/signup", methods=["POST"])
    async def signup(self):
        try:
            AuthRoutes._validateJsonRequest(request)

            email = request.json.get("email", None)
            password = request.json.get("password", None)

            AuthRoutes._validateEmailAndPassword(email, password)

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

    @blueprint.route("/validate-token", methods=["POST"])
    async def validateToken(self):
        try:
            AuthRoutes._validateJsonRequest(request)

            await self.auth_repository.validateToken()

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

    @blueprint.route("/validate-token", methods=["POST"])
    async def refreshToken(self):
        try:
            AuthRoutes._validateJsonRequest(request)

            await self.auth_repository.refreshToken()

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

    @staticmethod
    def _validateJsonRequest(request: Request):
        if not MissingJsonException.validate_request(request):
            return MissingJsonException().toJson(), 400

    @staticmethod
    def _validateEmailAndPassword(email: str, password: str):
        if not email:
            return MissingEmailException().toJson(), 400

        if not ValidateEmailMixin.validate_email(email):
            return InvalidEmailException().toJson(), 400

        if not password:
            return MissingPasswordException().toJson(), 400
