class FetchUserByTokenRequestDto:
    def __init__(
        self,
        token: str,
    ):
        self.token = token
