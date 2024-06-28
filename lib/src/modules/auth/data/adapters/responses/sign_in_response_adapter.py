import json

from lib.src.modules.auth.domain.dtos.responses.sign_in_response_dto import (
    SignInResponseDto,
)


class SignInResponseAdapter:
    @staticmethod
    def to_json(dto: SignInResponseDto) -> str:
        """
        Converts a SignInResponseDto instance to a JSON string.

        :param dto: The SignInResponseDto instance to convert.
        :return: A JSON string representation of the DTO.
        """
        return json.dumps(dto.__dict__)
