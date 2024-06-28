from lib.src.modules.auth.domain.entities.user_entity import UserEntity
from lib.src.modules.auth.domain.entities.user_role import UserRole


class ConsultationCompleteRequestDto:
    def __init__(
        self,
        id: int,
        user: UserEntity,
    ):
        self.id = id
        self.user = user
