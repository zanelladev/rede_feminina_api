import pyrebase
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from firebase_admin import auth


class AuthRepository(IAuthRepository):
    def __init__(self, firebase):
        self._firebase = firebase
        self.firebase_config = {
            "apiKey": "AIzaSyBxSOnMjKepRMs9f2sjH8pFWCZaCONjIKg",
            "authDomain": "redefemininacancerjgs.firebaseapp.com",
            "projectId": "redefemininacancerjgs",
            "storageBucket": "redefemininacancerjgs.appspot.com",
            "messagingSenderId": "294193398988",
            "appId": "1:294193398988:web:082689ee9346faa5fdee69",
            "measurementId": "G-9HG1H1JD5K",
            "databaseURL": "https://redefemininacancerjgs.firebaseio.com"
        }
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.auth = self.firebase.auth()

    async def signIn(self):
        try:
            user = self.auth.sign_in_with_email_and_password(
                "email@gmail.com", "password")
            print('Successfully signed in:', user)
            return user
        except Exception as e:
            print('Error signing in:', e)
            return None

    async def signUp(self):
        try:
            user = self.auth.create_user_with_email_and_password(
                "email@gmail.com", "password")
            print('Successfully signed up:', user)
            return user
        except Exception as e:
            print('Error signing up:', e)
            return None

    async def signOut(self):
        pass
