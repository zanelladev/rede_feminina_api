class FirebaseFactory:
    _instance = None

    @classmethod
    def init(cls):
        if cls._instance is None:
            cls._instance = cls.create()

    @staticmethod
    def create():
        instance = None

        return instance

    @property
    def instance(self):
        return self._instance
