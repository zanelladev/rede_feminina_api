from lib.src.app_routes import AppRoutes
from lib.src.core.factories.firebase.firebase_factory import FirebaseFactory
from lib.src.core.factories.flask.flask_factory import FlaskFactory
from lib.src.core.factories.mysql.mysql_factory import MySqlFactory
from lib.src.core.services.injector.injector import Injector
from lib.src.modules.auth.data.repositories.auth_repository import AuthRepository
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository
from lib.src.modules.auth.routes.auth_routes import AuthRoutes
from lib.src.modules.consultation.data.repositories.consultation_repository import (
    ConsultationRepository,
)
from lib.src.modules.consultation.domain.repositories.i_consultation_repository import (
    IConsultationRepository,
)
from lib.src.modules.consultation.routes.consultation_routes import ConsultationRoutes


class AppInjections:
    @staticmethod
    def registerBinds():
        Injector.register(
            FirebaseFactory,
            FirebaseFactory.instance(),
        )
        Injector.register(
            MySqlFactory,
            MySqlFactory(),
        )
        Injector.register(
            IAuthRepository,
            AuthRepository(
                Injector.retrieve(FirebaseFactory),
                Injector.retrieve(MySqlFactory),
            ),
        )
        Injector.register(
            AuthRoutes,
            AuthRoutes(
                Injector.retrieve(IAuthRepository),
            ),
        )
        Injector.register(
            IConsultationRepository,
            ConsultationRepository(
                Injector.retrieve(MySqlFactory),
            ),
        )
        Injector.register(
            ConsultationRoutes,
            ConsultationRoutes(
                Injector.retrieve(IConsultationRepository),
                Injector.retrieve(IAuthRepository),
            ),
        )

        Injector.register(
            AppRoutes,
            AppRoutes(
                Injector.retrieve(AuthRoutes),
                Injector.retrieve(ConsultationRoutes),
            ),
        )
        Injector.register(
            FlaskFactory,
            FlaskFactory.instance(
                Injector.retrieve(AppRoutes),
                Injector.retrieve(IAuthRepository),
            ),
        )
