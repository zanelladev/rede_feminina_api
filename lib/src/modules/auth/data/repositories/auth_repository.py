from lib.src.modules.auth.domain.dtos.sign_in_request_dto import SignInRequestDto
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRepository(IAuthRepository):
    def __init__(self, firebaseAuth):
        self.auth = firebaseAuth

    async def signIn(self, dto: SignInRequestDto):
        try:
            user = self.auth.sign_in_with_email_and_password(dto.email, dto.password)

            print("Successfully signed in:", user)
            return user
        except Exception as e:
            print("Error signing in:", e)
            return None

    async def signUp(self):
        try:
            user = self.auth.create_user_with_email_and_password(
                "email@gmail.com", "password"
            )

            print("Successfully signed up:", user)
            return user
        except Exception as e:
            print("Error signing up:", e)
            return None

    async def signOut(self):
        pass

    async def refreshToken(self, refreshToken: str):
        user = self.auth.refresh(refreshToken)

        return user

    async def validateToken(self, token: str):
        user = self.auth.get_account_info(token)

        return user
