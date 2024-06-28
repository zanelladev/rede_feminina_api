from http.client import HTTPException

from dateutil import parser
from flask import Blueprint, Request, jsonify, request

from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.mixins.validate_json_body_mixin import ValidateJsonBodyMixin
from lib.src.core.routes.app_route import AppRoute
from lib.src.modules.auth.domain.dtos.requests.fetch_user_by_token_request_dto import (
    FetchUserByTokenRequestDto,
)
from lib.src.modules.auth.domain.entities.user_role import UserRole
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from lib.src.modules.consultation.data.adapters.responses.consultation_complete_response_dto_adapter import (
    ConsultationCompleteResponseDtoAdapter,
)
from lib.src.modules.consultation.data.adapters.responses.consultation_create_response_dto_adapter import (
    ConsultationCreateResponseDtoAdapter,
)
from lib.src.modules.consultation.data.adapters.responses.consultation_edit_response_dto_adapter import (
    ConsultationEditResponseDtoAdapter,
)
from lib.src.modules.consultation.data.adapters.responses.consultation_fetch_all_response_dto_adapter import (
    ConsultationFetchAllResponseDtoAdapter,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_complete_request_dto import (
    ConsultationCompleteRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_create_request_dto import (
    ConsultationCreateRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_edit_request_dto import (
    ConsultationEditRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_fetch_all_request_dto import (
    ConsultationFetchAllRequestDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_fetch_all_response_dto import (
    ConsultationFetchAllResponseDto,
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
        self.blueprint.add_url_rule(
            "/edit",
            "edit",
            self.edit,
            methods=["PUT"],
        )
        self.blueprint.add_url_rule(
            "/complete",
            "complete",
            self.complete,
            methods=["PUT"],
        )
        self.blueprint.add_url_rule(
            "/fetch-all",
            "fetchAll",
            self.fetchAll,
            methods=["GET"],
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
                    date=parser.parse(request.json["date"]),
                    id_type=request.json["id_type"],
                )
            )

            return ConsultationCreateResponseDtoAdapter.to_json(response)

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

    async def edit(self):
        try:
            self._validateJsonRequest(request)

            user_response = await self.auth_repository.fetch_user_by_token(
                FetchUserByTokenRequestDto(token=request.headers.get("Authorization"))
            )

            response = await self.consultation_repository.edit(
                ConsultationEditRequestDto(
                    id=request.json["id"] if request.json.get("id") else None,
                    date=(
                        parser.parse(request.json["date"])
                        if request.json.get("date")
                        else None
                    ),
                    id_type=(
                        request.json["id_type"] if request.json.get("id_type") else None
                    ),
                    user=user_response.user,
                )
            )

            return ConsultationEditResponseDtoAdapter.to_json(response)

        except HTTPException as e:
            return jsonify(e.toJson()), 404

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to edit consultation.",
                        "error": str(e),
                    }
                ),
                400,
            )

    async def complete(self):
        try:
            self._validateJsonRequest(request)

            user_response = await self.auth_repository.fetch_user_by_token(
                FetchUserByTokenRequestDto(token=request.headers.get("Authorization"))
            )

            response = await self.consultation_repository.complete(
                ConsultationCompleteRequestDto(
                    id=request.json["id"],
                    user=user_response.user,
                )
            )

            return ConsultationCompleteResponseDtoAdapter.to_json(response)

        except HTTPException as e:
            return jsonify(e.toJson()), 404

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to complete consultation.",
                        "error": str(e),
                    }
                ),
                400,
            )

    async def fetchAll(self):
        try:
            self._validateJsonRequest(request)

            user_response = await self.auth_repository.fetch_user_by_token(
                FetchUserByTokenRequestDto(token=request.headers.get("Authorization"))
            )

            response = await self.consultation_repository.fetchAll(
                ConsultationFetchAllRequestDto(
                    start_date=parser.parse(request.json["start_date"]),
                    end_date=parser.parse(request.json["end_date"]),
                    user=user_response.user,
                )
            )

            return ConsultationFetchAllResponseDtoAdapter.to_json(response)

        except HTTPException as e:
            return jsonify(e.toJson()), 404

        except Exception as e:
            return (
                jsonify(
                    {
                        "msg": "An error occurred while trying to fetch all consultation.",
                        "error": str(e),
                    }
                ),
                400,
            )

    def _validateJsonRequest(self, request: Request):
        if not self.validate_json_body(request):
            raise MissingJsonException()
