import json

from lib.src.modules.auth.domain.dtos.requests.sign_up_request_dto import (
    SignUpRequestDto,
)


class SignUpRequestAdapter:
    @staticmethod
    def from_json(json_str: str) -> SignUpRequestDto:
        data = json.loads(json_str)
        return SignUpRequestDto(
            email=data.get("email"),
            password=data.get("password"),
            name=data.get("name"),
            surname=data.get("surname"),
            social_name=data.get("social_name"),
            cpf=data.get("cpf"),
            phone_number=data.get("phone_number"),
        )
