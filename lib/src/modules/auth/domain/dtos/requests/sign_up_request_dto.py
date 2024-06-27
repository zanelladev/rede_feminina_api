from typing import Optional


class SignUpRequestDto:
    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        surname: str,
        cpf: int,
        phone_number: int,
        social_name: Optional[str] = None,
    ):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.social_name = social_name
        self.cpf = cpf
        self.phone_number = phone_number
