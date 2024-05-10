class UserEntity:
    def __init__(self, userId, email):
        if userId is None or email is None:
            raise ValueError("userId and email are required.")
        self.userId = userId
        self.email = email


UserEntity(userId=1)
