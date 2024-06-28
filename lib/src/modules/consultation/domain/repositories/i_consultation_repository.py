from abc import ABC, abstractmethod

from lib.src.modules.consultation.domain.dtos.requests.consultation_complete_request_dto import (
    ConsultationCompleteRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_create_request_dto import (
    ConsultationCreateRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_edit_request_dto import (
    ConsultationEditRequestDto,
)
from lib.src.modules.consultation.domain.dtos.requests.consultation_fetch_all_request_dto import (
    ConsultationFetchAllRequestDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_complete_response_dto import (
    ConsultationCompleteResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_create_response_dto import (
    ConsultationCreateResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_edit_response_dto import (
    ConsultationEditResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_fetch_all_response_dto import (
    ConsultationFetchAllResponseDto,
)


class IConsultationRepository(ABC):
    @abstractmethod
    async def create(
        self, dto: ConsultationCreateRequestDto
    ) -> ConsultationCreateResponseDto:
        pass

    @abstractmethod
    async def edit(
        self, dto: ConsultationEditRequestDto
    ) -> ConsultationEditResponseDto:
        pass

    @abstractmethod
    async def fetchAll(
        self, dto: ConsultationFetchAllRequestDto
    ) -> ConsultationFetchAllResponseDto:
        pass

    @abstractmethod
    async def complete(
        self, dto: ConsultationCompleteRequestDto
    ) -> ConsultationCompleteResponseDto:
        pass
