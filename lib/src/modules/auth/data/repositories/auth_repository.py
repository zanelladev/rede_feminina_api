from lib.src.modules.auth.domain.dtos.requests.refresh_token_request_dto import (
    RefreshTokenRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.sign_in_request_dto import (
    SignInRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.sign_up_request_dto import (
    SignUpRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.validate_token_request_dto import (
    ValidateTokenRequestDto,
)
from lib.src.modules.auth.domain.dtos.responses.refresh_token_response_dto import (
    RefreshTokenResponseDto,
)
from lib.src.modules.auth.domain.dtos.responses.sign_in_response_dto import (
    SignInResponseDto,
)
from lib.src.modules.auth.domain.dtos.responses.sign_up_response_dto import (
    SignUpResponseDto,
)
from lib.src.modules.auth.domain.dtos.responses.validate_token_response_dto import (
    ValidateTokenResponseDto,
)
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRepository(IAuthRepository):
    def __init__(self, firebaseAuth):
        self.auth = firebaseAuth

    async def signIn(self, dto: SignInRequestDto) -> SignInResponseDto:
        try:
            user = self.auth.sign_in_with_email_and_password(dto.email, dto.password)

            return SignInResponseDto(
                email=user["email"],
                refresh_token=user["refreshToken"],
                id_token=user["idToken"],
                cpf="",
                name="",
                surname="",
                social_name="",
                phone_number="",
            )

        except Exception as e:
            return None

    async def signUp(self, dto: SignUpRequestDto) -> SignUpResponseDto:
        try:
            user = self.auth.create_user_with_email_and_password(
                dto.email, dto.password
            )

            return SignUpResponseDto(
                email=user["email"],
                refresh_token=user["refreshToken"],
                id_token=user["idToken"],
                cpf="",
                name="",
                surname="",
                social_name="",
                phone_number="",
            )

        except Exception as e:
            print("Error signing up:", e)
            return None

    async def refreshToken(
        self, dto: RefreshTokenRequestDto
    ) -> RefreshTokenResponseDto:
        user = self.auth.refresh(dto.refresh_token)

        return RefreshTokenResponseDto(token=user["idToken"])

    async def validateToken(
        self, dto: ValidateTokenRequestDto
    ) -> ValidateTokenResponseDto:

        try:
            user = self.auth.get_account_info(dto.token)

            if user is None:
                return ValidateTokenResponseDto(is_valid=False)

            return ValidateTokenResponseDto(is_valid=True)
        except Exception as e:
            print(f"Error validating token: {e}")
            return ValidateTokenResponseDto(is_valid=False)
