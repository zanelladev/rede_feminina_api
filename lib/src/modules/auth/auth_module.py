from injector import Module, singleton
from lib.src.modules.auth.data.repositories.auth_repository import AuthRepository
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthModule(Module):
    def configure(self, binder):
        binder.bind(IAuthRepository, to=AuthRepository, scope=singleton)
