from datetime import datetime
from typing import Optional

from lib.src.modules.auth.domain.entities.user_entity import UserEntity


class ConsultationFetchEntity:
    def __init__(
        self,
        id: int,
        date: datetime,
        is_completed: bool,
        id_type: int,
        user: Optional[UserEntity] = None,
    ):
        self.id = id
        self.date = date
        self.is_completed = is_completed
        self.id_type = id_type
        self.user = user
