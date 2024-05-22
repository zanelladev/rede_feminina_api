from lib.src.app_injections import AppInjections
from lib.src.core.factories.flask.flask_factory import FlaskFactory
from lib.src.core.services.injector.injector import Injector

AppInjections.registerBinds()
app = Injector.retrieve(FlaskFactory)

if __name__ == "__main__":
    app.run()
