import json

from lib.src.modules.auth.domain.dtos.responses.refresh_token_response_dto import (
    RefreshTokenResponseDto,
)


class RefreshTokenResponseAdapter:
    @staticmethod
    def to_json(dto: RefreshTokenResponseDto) -> str:
        """
        Converts a RefreshTokenResponseDto instance to a JSON string.

        :param dto: The RefreshTokenResponseDto instance to convert.
        :return: A JSON string representation of the dto.
        """
        data = {"token": dto.token}
        return json.dumps(data)
