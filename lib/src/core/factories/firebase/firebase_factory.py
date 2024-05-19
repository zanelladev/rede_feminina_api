import firebase_admin
from firebase_admin import credentials


class FirebaseFactory:
    _instance = None

    @classmethod
    def init(cls):
        if cls._instance is None:
            cls._instance = cls._create()

        return cls._instance

    @staticmethod
    def _create():
        cred = credentials.Certificate("firebase_credentials.json")
        instance = firebase_admin.initialize_app(cred)

        return instance

    @property
    def instance(self):
        return self._instance
