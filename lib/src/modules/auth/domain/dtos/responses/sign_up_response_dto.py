from typing import Optional


class SignUpResponseDto:
    def __init__(
        self,
        id: int,
        email: str,
        name: str,
        surname: str,
        cpf: str,
        phone_number: int,
        id_token: str,
        refresh_token: str,
        social_name: Optional[str] = None,
    ):
        self.id = id
        self.email = email
        self.name = name
        self.surname = surname
        self.cpf = cpf
        self.phone_number = phone_number
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.social_name = social_name