from typing import Optional

from lib.src.modules.auth.domain.entities.user_role import UserRole


class UserEntity:
    def __init__(
        self,
        id: int,
        email: str,
        name: str,
        surname: str,
        cpf: str,
        phone_number: int,
        role: UserRole,
        social_name: Optional[str] = None,
    ):
        self.id = id
        self.email = email
        self.name = name
        self.surname = surname
        self.cpf = cpf
        self.phone_number = phone_number
        self.role = role
        self.social_name = social_name
