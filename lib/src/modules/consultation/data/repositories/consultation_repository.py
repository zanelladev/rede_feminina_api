from lib.src.core.factories.mysql.mysql_factory import MySqlFactory
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
from lib.src.modules.consultation.domain.dtos.responses.consultation_create_response_dto import (
    ConsultationCreateResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_edit_response_dto import (
    ConsultationEditResponseDto,
)
from lib.src.modules.consultation.domain.dtos.responses.consultation_fetch_all_response_dto import (
    ConsultationFetchAllResponseDto,
)
from lib.src.modules.consultation.domain.repositories.i_consultation_repository import (
    IConsultationRepository,
)


class ConsultationRepository(IConsultationRepository):
    def __init__(self, mysql_factory: MySqlFactory):
        self.mysql_factory = mysql_factory

    async def create(
        self, dto: ConsultationCreateRequestDto
    ) -> ConsultationCreateResponseDto:
        pass

    async def edit(
        self, dto: ConsultationEditRequestDto
    ) -> ConsultationEditResponseDto:
        pass

    async def fetchAll(
        self, dto: ConsultationFetchAllRequestDto
    ) -> ConsultationFetchAllResponseDto:
        pass

    async def complete(
        self, dto: ConsultationCompleteRequestDto
    ) -> ConsultationCompleteRequestDto:

        pass
