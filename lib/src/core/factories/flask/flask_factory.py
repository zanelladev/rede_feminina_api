from flask import Flask
from flask_cors import CORS

from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class FlaskFactory:
    _app = None

    @classmethod
    def init(cls):
        if cls._app is None:
            cls._app = cls.create_app()

        return cls._app

    @staticmethod
    def create_app():
        app = Flask(__name__)

        FlaskFactory._register_blueprints(app)

        CORS(app)

        @app.route('/')
        def index():
            return '<h1>Aplicacao server-side</h1>'

        return app

    @staticmethod
    def _register_blueprints(app: Flask):
        app.register_blueprint(AuthRoutes.blueprint)

        return

    @property
    def app(self):
        return self._app
