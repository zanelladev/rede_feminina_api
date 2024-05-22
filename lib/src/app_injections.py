from lib.src.core.factories.firebase.firebase_factory import FirebaseFactory
from lib.src.core.factories.flask.flask_factory import FlaskFactory
from lib.src.core.services.injector.injector import Injector
from lib.src.modules.auth.data.repositories.auth_repository import AuthRepository
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class AppInjections:
    @staticmethod
    def registerBinds():
        Injector.register(FirebaseFactory, FirebaseFactory.instance())
        Injector.register(
            IAuthRepository, AuthRepository(Injector.retrieve(FirebaseFactory))
        )
        Injector.register(
            IAuthRepository, AuthRepository(Injector.retrieve(FirebaseFactory))
        )
        Injector.register(
            AuthRoutes,
            AuthRoutes(Injector.retrieve(IAuthRepository)),
        )
        Injector.register(
            FlaskFactory,
            FlaskFactory.instance(Injector.retrieve(AuthRoutes)),
        )
