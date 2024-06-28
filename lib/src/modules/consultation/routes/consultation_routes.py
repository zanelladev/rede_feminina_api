from http.client import HTTPException

from flask import Blueprint, Request, jsonify, request

from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.mixins.validate_json_body_mixin import ValidateJsonBodyMixin
from lib.src.core.routes.app_route import AppRoute
from lib.src.modules.auth.domain.dtos.requests.fetch_user_by_token_request_dto import (
    FetchUserByTokenRequestDto,
)
from lib.src.modules.auth.domain.entities.user_role import UserRole
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from lib.src.modules.consultation.domain.dtos.requests.consultation_create_request_dto import (
    ConsultationCreateRequestDto,
)
from lib.src.modules.consultation.domain.repositories.i_consultation_repository import (
    IConsultationRepository,
)


class ConsultationRoutes(AppRoute, ValidateJsonBodyMixin):
    def __init__(
        self,
        consultation_repository: IConsultationRepository,
        auth_repository: IAuthRepository,
    ):
        self.required_authorization = True
        self.name = "consultation"
        self.consultation_repository = consultation_repository
        self.auth_repository = auth_repository
        self.blueprint = Blueprint(self.name, __name__, url_prefix=f"/{self.name}")
        self._register_routes()
        super().__init__(self.required_authorization, self.name, self.blueprint)

    def _register_routes(self):
        self.blueprint.add_url_rule(
            "/create",
            "create",
            self.create,
            methods=["POST"],
        )

    async def create(self):
        try:
            self._validateJsonRequest(request)

            user_response = await self.auth_repository.fetch_user_by_token(
                FetchUserByTokenRequestDto(token=request.headers.get("Authorization"))
            )

            response = await self.consultation_repository.create(
                ConsultationCreateRequestDto(
                    id_user=user_response.user.id,
                    user_role=user_response.user.role,
                    date=request.json["date"],
                    id_type=request.json["id_type"],
                )
            )

        except HTTPException as e:
            return jsonify(e.toJson()), 404

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to create consultation.",
                        "error": str(e),
                    }
                ),
                400,
            )

    def _validateJsonRequest(self, request: Request):
        if not self.validate_json_body(request):
            raise MissingJsonException()
