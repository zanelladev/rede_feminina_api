from flask import Flask

from lib.src.modules.auth.routes.auth_routes import AuthRoutes
from lib.src.modules.consultation.routes.consultation_routes import ConsultationRoutes


class AppRoutes:
    def __init__(
        self, auth_routes: AuthRoutes, consultation_routes: ConsultationRoutes
    ):
        self.routes = [
            auth_routes,
            consultation_routes,
        ]

    def registerRoutes(self, app: Flask):
        for route in self.routes:
            app.register_blueprint(route.blueprint)

    def currentRouteNeedAuth(self, current_endpoint: str):
        for route in self.routes:
            if route.name in current_endpoint and route.required_authorization:
                return route

        return None
