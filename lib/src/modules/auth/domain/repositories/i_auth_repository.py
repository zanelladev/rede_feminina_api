from abc import ABC, abstractmethod


class IAuthRepository(ABC):
    @abstractmethod
    async def signIn(self): pass

    @abstractmethod
    async def signUp(self): pass

    @abstractmethod
    async def signOut(self): pass
