import json

from lib.src.modules.auth.domain.dtos.responses.validate_token_response_dto import (
    ValidateTokenResponseDto,
)


class ValidateTokenResponseAdapter:
    @staticmethod
    def to_json(dto: ValidateTokenResponseDto) -> str:
        """
        Converts a ValidateTokenResponseDto instance to a JSON string.

        :param dto: The ValidateTokenResponseDto instance to convert.
        :return: A JSON string representation of the dto.
        """
        data = {"is_valid": dto.is_valid}
        return json.dumps(data)
