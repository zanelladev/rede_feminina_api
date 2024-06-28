from lib.src.modules.auth.domain.entities.user_role import UserRole


class ConsultationCompleteRequestDto:
    def __init__(
        self,
        id: int,
        id_user: int,
        user_role: UserRole,
    ):
        self.id = id
        self.id_user = id_user
        self.user_role = user_role
