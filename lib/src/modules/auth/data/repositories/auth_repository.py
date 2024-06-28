from lib.src.core.factories.mysql.mysql_factory import MySqlFactory
from lib.src.modules.auth.domain.dtos.requests.fetch_user_by_token_request_dto import (
    FetchUserByTokenRequestDto,
)
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
from lib.src.modules.auth.domain.dtos.responses.fetch_user_by_token_response_dto import (
    FetchUserByTokenResponseDto,
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
from lib.src.modules.auth.domain.entities.user_entity import UserEntity
from lib.src.modules.auth.domain.entities.user_role import UserRole
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRepository(IAuthRepository):
    def __init__(self, firebaseAuth, mysql_factory: MySqlFactory):
        self.auth = firebaseAuth
        self.mysql_factory = mysql_factory

    async def signIn(self, dto: SignInRequestDto) -> SignInResponseDto:
        try:
            user = self.auth.sign_in_with_email_and_password(dto.email, dto.password)
            sql_result = await self.fetch_user_by_id_firebase(user["localId"])

            return SignInResponseDto(
                id=sql_result["id"],
                email=sql_result["email"],
                refresh_token=user["refreshToken"],
                id_token=user["idToken"],
                cpf=sql_result["cpf"],
                name=sql_result["name"],
                surname=sql_result["surname"],
                social_name=sql_result["social_name"],
                phone_number=sql_result["phone_number"],
            )

        except Exception as e:
            return None

    async def signUp(self, dto: SignUpRequestDto) -> SignUpResponseDto:
        try:
            user = self.auth.create_user_with_email_and_password(
                dto.email, dto.password
            )

            self.mysql_factory.connect()
            sql = "INSERT INTO user (id_firebase, name, surname, social_name, cpf, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (
                user["localId"],
                dto.name,
                dto.surname,
                dto.social_name,
                dto.cpf,
                str(dto.phone_number),
                dto.email,
            )

            sql_cursor = self.mysql_factory.get_cursor()
            sql_cursor.execute(sql, val)

            self.mysql_factory.commit()
            self.mysql_factory.close_connection()

            sql_result = await self.fetch_user_by_id_firebase(user["localId"])

            return SignUpResponseDto(
                id=sql_result["id"],
                email=sql_result["email"],
                refresh_token=user["refreshToken"],
                id_token=user["idToken"],
                cpf=sql_result["cpf"],
                name=sql_result["name"],
                surname=sql_result["surname"],
                social_name=sql_result["social_name"],
                phone_number=sql_result["phone_number"],
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

    async def fetch_user_by_token(
        self, dto: FetchUserByTokenRequestDto
    ) -> FetchUserByTokenResponseDto:
        firebase_user = self.auth.get_account_info(dto.token)
        sql_user = await self.fetch_user_by_id_firebase(
            firebase_user["users"][0]["localId"]
        )

        return FetchUserByTokenResponseDto(
            user=UserEntity(
                id=sql_user["id"],
                email=sql_user["email"],
                cpf=sql_user["cpf"],
                name=sql_user["name"],
                surname=sql_user["surname"],
                social_name=sql_user["social_name"],
                phone_number=sql_user["phone_number"],
                role=UserRole(sql_user["role"]),
            )
        )

    async def fetch_user_by_id_firebase(self, id_firebase):
        try:
            self.mysql_factory.connect()
            cursor = self.mysql_factory.get_cursor()
            sql = "SELECT * FROM user WHERE id_firebase = %s"
            val = (id_firebase,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            return result
        finally:
            cursor.close()
            self.mysql_factory.close_connection()
