from http.client import HTTPException

from flask import Blueprint, Request, jsonify, request

from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.mixins.validate_email_mixin import ValidateEmailMixin
from lib.src.core.mixins.validate_json_body_mixin import ValidateJsonBodyMixin
from lib.src.core.routes.app_route import AppRoute
from lib.src.modules.auth.data.adapters.requests.sign_in_request_adapter import (
    SignInRequestAdapter,
)
from lib.src.modules.auth.data.adapters.responses.refresh_token_response_adapter import (
    RefreshTokenResponseAdapter,
)
from lib.src.modules.auth.data.adapters.responses.sign_in_response_adapter import (
    SignInResponseAdapter,
)
from lib.src.modules.auth.data.adapters.responses.sign_up_response_adapter import (
    SignUpResponseAdapter,
)
from lib.src.modules.auth.data.adapters.responses.validate_token_response_adapter import (
    ValidateTokenResponseAdapter,
)
from lib.src.modules.auth.domain.dtos.requests.refresh_token_request_dto import (
    RefreshTokenRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.sign_in_request_dto import (
    SignInRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.sign_up_request_dto import (
    SignUpRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.validate_token_request_dto import (
    ValidateTokenRequestDto,
)
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


class AuthRoutes(AppRoute, ValidateEmailMixin, ValidateJsonBodyMixin):
    def __init__(self, auth_repository: IAuthRepository):
        self.required_authorization = False
        self.name = "auth"
        self.auth_repository = auth_repository
        self.blueprint = Blueprint(self.name, __name__, url_prefix=f"/{self.name}")
        self._register_routes()
        super().__init__(self.required_authorization, self.name, self.blueprint)

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

            if user:
                return SignInResponseAdapter.to_json(user), 200

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
            name = request.json.get("name", None)
            surname = request.json.get("surname", None)
            cpf = request.json.get("cpf", None)
            phone_number = request.json.get("phone_number", None)
            social_name = request.json.get("social_name", None)

            self._validateEmailAndPassword(email, password)

            dto = SignUpRequestDto(
                email,
                password,
                name,
                surname,
                cpf,
                phone_number,
                social_name,
            )

            user = await self.auth_repository.signUp(dto)

            return SignUpResponseAdapter.to_json(user), 200

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

            token = request.json.get("token", None)

            dto = ValidateTokenRequestDto(token=token)

            response = await self.auth_repository.validateToken(dto)

            return ValidateTokenResponseAdapter.to_json(response), 200

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

            refresh_token = request.json.get("refresh_token", None)

            dto = RefreshTokenRequestDto(refresh_token=refresh_token)

            response = await self.auth_repository.refreshToken(dto)

            return RefreshTokenResponseAdapter.to_json(response), 200

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
