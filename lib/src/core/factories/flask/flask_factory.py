from flask import Flask, abort
from flask_cors import CORS

from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class FlaskFactory:
    _app = None

    @classmethod
    def instance(cls, auth_routes: AuthRoutes):
        """Retorna uma instância única do aplicativo Flask.

        Args:
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.

        Returns:
            Flask: Instância do aplicativo Flask.
        """
        if cls._app is None:
            cls._app = cls.create_app(auth_routes)
        return cls._app

    @staticmethod
    def create_app(auth_routes: AuthRoutes) -> Flask:
        """Cria e configura o aplicativo Flask.

        Args:
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.

        Returns:
            Flask: Instância do aplicativo Flask configurada.
        """
        app = Flask(__name__)

        # Registra os blueprints
        FlaskFactory._register_blueprints(app, auth_routes)

        # Configura o CORS
        CORS(app)

        @app.route("/")
        def index():
            return "<h1>Aplicacao server-side</h1>"

        # @app.before_request
        # def before_request():
        #     """Executa antes de cada requisição."""
        #     if "user_id" not in session:
        #         # If the user is not logged in, abort the request with a 401 Unauthorized status
        #         abort(401, description="Unauthorized: Session is invalid or expired.")

        return app

    @staticmethod
    def _register_blueprints(app: Flask, auth_routes: AuthRoutes):
        """Registra os blueprints no aplicativo Flask.

        Args:
            app (Flask): Instância do aplicativo Flask.
            auth_routes (AuthRoutes): Objeto contendo as rotas de autenticação.
        """
        app.register_blueprint(auth_routes.blueprint)
