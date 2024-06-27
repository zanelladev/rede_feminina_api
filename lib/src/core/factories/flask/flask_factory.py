from flask import Flask, abort, request
from flask_cors import CORS

from lib.src.app_routes import AppRoutes
from lib.src.core.exceptions.http_exception import HttpException
from lib.src.core.exceptions.invalid_token_exception import InvalidTokenException
from lib.src.core.exceptions.missing_token_exception import MissingTokenException
from lib.src.modules.auth.data.repositories.auth_repository import AuthRepository
from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class FlaskFactory:
    _app = None

    @classmethod
    def instance(cls, routes: AppRoutes, authRepository: AuthRepository):
        """Retorna uma instância única do aplicativo Flask.

        Args:
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.

        Returns:
            Flask: Instância do aplicativo Flask.
        """
        if cls._app is None:
            cls._app = cls.create_app(routes, authRepository)
        return cls._app

    @staticmethod
    def create_app(routes: AppRoutes, authRepository: AuthRepository) -> Flask:
        """Cria e configura o aplicativo Flask.

        Args:
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.

        Returns:
            Flask: Instância do aplicativo Flask configurada.
        """
        app = Flask(__name__)

        # Registra os blueprints
        routes.registerRoutes(app)

        # Configura o CORS
        CORS(app)

        @app.route("/")
        def index():
            return "<h1>Aplicacao server-side</h1>"

        @app.before_request
        async def before_request():
            try:
                if not routes.currentRouteNeedAuth(request.path):
                    return None

                if "Authorization" not in request.headers:
                    raise MissingTokenException()

                valid = await authRepository.validateToken(
                    request.headers.get("Authorization")
                )

                if not valid:
                    raise InvalidTokenException()

            except HttpException as e:
                return e.toJson(), 401

            except Exception as e:
                return {"error": str(e)}, 500

        return app

    @staticmethod
    def _register_blueprints(app: Flask, auth_routes: AuthRoutes):
        """Registra os blueprints no aplicativo Flask.

        Args:
            app (Flask): Instância do aplicativo Flask.
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.
        """
        app.register_blueprint(auth_routes.blueprint)
