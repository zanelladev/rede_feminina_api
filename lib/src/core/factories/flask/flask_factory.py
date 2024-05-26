from flask import Flask
from flask_cors import CORS

from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class FlaskFactory:
    _app = None

    @classmethod
    def instance(self, auth_routes: AuthRoutes):
        self.auth_routes = auth_routes
        if self._app is None:
            self._app = self.create_app(self)

        return self._app

    @staticmethod
    def create_app(self):
        app = Flask(__name__)

        self._register_blueprints(self, app)

        CORS(app)

        @app.route("/")
        def index():
            return "<h1>Aplicacao server-side</h1>"

        return app

    @staticmethod
    def _register_blueprints(self, app: Flask):
        app.register_blueprint(self.auth_routes.blueprint)
        return
