from lib.src.app_injections import AppInjections
from lib.src.core.factories.flask.flask_factory import FlaskFactory

AppInjections.registerBinds()
app = FlaskFactory.create_app()

if __name__ == "__main__":
    app.run()
