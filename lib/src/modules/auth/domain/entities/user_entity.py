class UserEntity:
    def __init__(self, userId: str, email: str, password: str, name: str, surname: str):
        if (
            userId is None
            or email is None
            or password is None
            or name is None
            or surname is None
        ):
            raise ValueError("userId, email, password, name and surname are required.")
        self.userId = userId
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
