import json

from lib.src.modules.auth.domain.dtos.responses.sign_up_response_dto import (
    SignUpResponseDto,
)


class SignUpResponseAdapter:
    @staticmethod
    def to_json(dto: SignUpResponseDto) -> str:
        """
        Converts a SignUpResponseDto instance to a JSON string.

        :param dto: The SignUpResponseDto instance to convert.
        :return: A JSON string representation of the DTO.
        """
        return json.dumps(dto.__dict__)
