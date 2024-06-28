from datetime import datetime

from lib.src.modules.auth.domain.entities.user_entity import UserEntity
from lib.src.modules.auth.domain.entities.user_role import UserRole


class ConsultationEditRequestDto:
    def __init__(
        self,
        id: int,
        date: datetime,
        id_type: int,
        user: UserEntity,
    ):
        self.id = id
        self.date = date
        self.id_type = id_type
        self.user = user
