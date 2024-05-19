from lib.src.core.services.injector.injector import Injector
from lib.src.modules.auth.data.repositories.auth_repository import AuthRepository
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AppInjections:
    @staticmethod
    def registerBinds():
        Injector.register(IAuthRepository, AuthRepository())
