import json

from lib.src.modules.consultation.domain.dtos.responses.consultation_complete_response_dto import (
    ConsultationCompleteResponseDto,
)


class ConsultationCompleteResponseDtoAdapter:
    @staticmethod
    def to_json(dto: ConsultationCompleteResponseDto) -> str:
        data = {
            "success": dto.success,
        }
        return json.dumps(data)
