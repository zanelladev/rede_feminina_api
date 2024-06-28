import json

from lib.src.modules.consultation.domain.dtos.responses.consultation_create_response_dto import (
    ConsultationCreateResponseDto,
)


class ConsultationCreateResponseDtoAdapter:
    @staticmethod
    def to_json(dto: ConsultationCreateResponseDto) -> str:
        data = {
            "id": dto.id,
            "date": dto.date.isoformat(),
            "is_completed": dto.is_completed,
        }
        return json.dumps(data)
