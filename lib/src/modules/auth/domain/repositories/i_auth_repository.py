from abc import ABC, abstractmethod

from lib.src.modules.auth.domain.dtos.sign_in_request_dto import SignInRequestDto


class IAuthRepository(ABC):
    @abstractmethod
    async def signIn(self, dto: SignInRequestDto):
        pass

    @abstractmethod
    async def signUp(self):
        pass

    @abstractmethod
    async def signOut(self):
        pass

    @abstractmethod
    async def validateToken(self, token: str):
        pass

    @abstractmethod
    async def refreshToken(self, refreshToken: str):
        pass
