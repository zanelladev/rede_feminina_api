import json

from lib.src.modules.consultation.domain.dtos.responses.consultation_edit_response_dto import (
    ConsultationEditResponseDto,
)


class ConsultationEditResponseDtoAdapter:
    @staticmethod
    def to_json(dto: ConsultationEditResponseDto) -> str:
        data = {
            "success": dto.success,
        }
        return json.dumps(data)
