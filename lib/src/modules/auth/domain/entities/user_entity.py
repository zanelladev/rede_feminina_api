class UserEntity:
    def __init__(self, userId: str, email: str, password: str):
        if userId is None or email is None or password is None:
            raise ValueError("userId, email, and password are required.")
        self.userId = userId
        self.email = email
        self.password = password
