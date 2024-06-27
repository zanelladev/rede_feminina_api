import json

from lib.src.modules.auth.domain.dtos.requests.refresh_token_request_dto import (
    RefreshTokenRequestDto,
)


class RefreshTokenRequestAdapter:
    @staticmethod
    def from_json(json_str: str) -> RefreshTokenRequestDto:
        """
        Converts a JSON string to a RefreshTokenRequestDto instance.

        :param json_str: JSON string containing the refresh token.
        :return: RefreshTokenRequestDto instance.
        :raises ValueError: If the refresh token is missing or invalid.
        """
        data = json.loads(json_str)
        refresh_token = data.get("refresh_token")
        return RefreshTokenRequestDto(refresh_token=refresh_token)
