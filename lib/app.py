from lib.src.app_injections import AppInjections
from lib.src.core.flask.server import Server

AppInjections.registerBinds()
app = Server.create_app()

if __name__ == "__main__":
    app.run()
