import json

from lib.src.modules.auth.data.entity.user_entity_adapter import UserEntityAdapter
from lib.src.modules.consultation.domain.dtos.responses.consultation_fetch_all_response_dto import (
    ConsultationFetchAllResponseDto,
)
from lib.src.modules.consultation.domain.entities.consultation_fetch_entity import (
    ConsultationFetchEntity,
)


class ConsultationFetchAllResponseDtoAdapter:
    @staticmethod
    def to_json(dto: ConsultationFetchAllResponseDto) -> str:
        consultations_list = [
            ConsultationFetchAllResponseDtoAdapter.dict(consultation)
            for consultation in dto.consultations
        ]
        return json.dumps({"consultations": consultations_list})

    # Exemplo de implementação do método to_dict() na classe ConsultationFetchEntity
    # Adicione este método dentro da classe ConsultationFetchEntity
    @staticmethod
    def dict(entity: ConsultationFetchEntity) -> dict:
        # Converta todos os atributos relevantes da entidade para um dicionário
        return {
            "id": entity.id,
            "date": entity.date.isoformat(),
            "is_completed": entity.is_completed,
            **(
                {"user": UserEntityAdapter.to_dict(entity.user)}
                if entity.user is not None
                else {}
            ),
            "id_type": entity.id_type,
        }
