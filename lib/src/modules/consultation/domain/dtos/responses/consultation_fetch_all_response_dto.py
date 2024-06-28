from typing import List

from lib.src.modules.consultation.domain.entities.consultation_fetch_entity import (
    ConsultationFetchEntity,
)


class ConsultationFetchAllResponseDto:
    def __init__(
        self,
        consultations: List[ConsultationFetchEntity],
    ):
        self.consultations = consultations
