from datetime import datetime

from lib.src.modules.auth.domain.entities.user_role import UserRole


class ConsultationEditRequestDto:
    def __init__(
        self,
        id: int,
        date: datetime,
        id_type: int,
        id_user: int,
        user_role: UserRole,
    ):
        self.id = id
        self.date = date
        self.id_type = id_type
        self.id_user = id_user
        self.user_role = user_role
