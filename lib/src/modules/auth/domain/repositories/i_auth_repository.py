from abc import ABC, abstractmethod


class IAuthRepository(ABC):
    @abstractmethod
    def signIn(self, entity):
        pass

    @abstractmethod
    def signUp(self, entity):
        pass

    @abstractmethod
    def signOut(self, entity):
        pass
