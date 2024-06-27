from typing import Optional


class SignInResponseDto:
    def __init__(
        self,
        email: str,
        name: str,
        surname: str,
        cpf: int,
        phone_number: int,
        id_token: str,
        refresh_token: str,
        social_name: Optional[str] = None,
    ):
        self.email = email
        self.name = name
        self.surname = surname
        self.cpf = cpf
        self.phone_number = phone_number
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.social_name = social_name
