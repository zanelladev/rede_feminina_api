from typing import Optional

from lib.src.modules.auth.domain.entities.user_entity import UserEntity


class FetchUserByTokenResponseDto:
    def __init__(
        self,
        user: UserEntity,
    ):
        self.user = user
