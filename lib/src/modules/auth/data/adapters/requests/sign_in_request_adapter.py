import json

from lib.src.modules.auth.domain.dtos.requests.sign_in_request_dto import (
    SignInRequestDto,
)


class SignInRequestAdapter:
    @staticmethod
    def from_json(json_str: str) -> SignInRequestDto:
        data = json.loads(json_str)
        return SignInRequestDto(
            email=data.get("email"),
            password=data.get("password"),
        )
