from abc import ABC, abstractmethod

from lib.src.modules.auth.domain.dtos.requests.sign_in_request_dto import (
    SignInRequestDto,
)
from lib.src.modules.auth.domain.dtos.requests.sign_up_request_dto import (
    SignUpRequestDto,
)
from lib.src.modules.auth.domain.dtos.responses.sign_in_response_dto import (
    SignInResponseDto,
)
from lib.src.modules.auth.domain.dtos.responses.sign_up_response_dto import (
    SignUpResponseDto,
)


class IAuthRepository(ABC):
    @abstractmethod
    async def signIn(self, dto: SignInRequestDto) -> SignInResponseDto:
        pass

    @abstractmethod
    async def signUp(self, dto: SignUpRequestDto) -> SignUpResponseDto:
        pass

    @abstractmethod
    async def validateToken(self, token: str):
        pass

    @abstractmethod
    async def refreshToken(self, refreshToken: str):
        pass
