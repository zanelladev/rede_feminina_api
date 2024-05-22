import json
import os

import pyrebase

from lib.src.core.factories.firebase.constants.firebase_constants import (
    FirebaseConstants,
)


class FirebaseFactory:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls._create()

        return cls._instance

    @staticmethod
    def _create():
        project_path = os.getcwd()
        firebase_config_path = os.path.join(
            project_path, FirebaseConstants.firebase_config_path
        )

        with open(firebase_config_path) as f:
            firebase_config = json.load(f)

        firebase = pyrebase.initialize_app(firebase_config)
        auth = firebase.auth()

        return auth
