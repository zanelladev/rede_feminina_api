from datetime import datetime

from lib.src.modules.auth.domain.entities.user_role import UserRole


class ConsultationFetchAllRequestDto:
    def __init__(
        self,
        start_date: datetime,
        end_date: datetime,
        user_role: UserRole,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.user_role = user_role
