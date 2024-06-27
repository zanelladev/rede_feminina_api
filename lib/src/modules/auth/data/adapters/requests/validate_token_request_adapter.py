import json
from typing import Any, Dict

from lib.src.modules.auth.domain.dtos.requests.validate_token_request_dto import (
    ValidateTokenRequestDto,
)


class ValidateTokenRequestAdapter:
    @staticmethod
    def from_json(json_str: str) -> ValidateTokenRequestDto:
        """
        Converts a JSON string to a ValidateTokenRequestDto instance.

        :param json_str: JSON string containing the token.
        :return: ValidateTokenRequestDto instance.
        :raises ValueError: If the token is missing or invalid.
        """
        data: Dict[str, Any] = json.loads(json_str)
        token: str = data.get("token")
        return ValidateTokenRequestDto(token=token)
