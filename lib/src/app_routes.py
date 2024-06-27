from flask import Flask

from lib.src.modules.auth.routes.auth_routes import AuthRoutes


class AppRoutes:
    def __init__(self, auth_routes: AuthRoutes):
        self.auth_routes = auth_routes
        self.routes = [
            self.auth_routes,
        ]

    def registerRoutes(self, app: Flask):
        for route in self.routes:
            app.register_blueprint(route.blueprint)

    def currentRouteNeedAuth(self, current_endpoint: str):
        for route in self.routes:
            if route.name in current_endpoint and route.required_authorization:
                return route

        return None
