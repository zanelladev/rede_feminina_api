from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from firebase_admin import auth


class AuthRepository(IAuthRepository):
    _firebase = None

    def __init__(self, firebase):
        self._firebase = firebase

    async def signIn(self):
        auth.sign_in_with_email_and_password("email", "password")

        print("Sign in")

    async def signUp(self):
        auth.create_user(email="email@gmail.com", password="password")

    async def signOut(self):
        pass
