from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class UserRepository(IAuthRepository):
    def signIn(self, entity):
        pass

    def signUp(self, entity):
        pass

    def signOut(self, entity):
        pass
