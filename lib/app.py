from lib.src.app_injections import AppInjections
from lib.src.core.factories.firebase.firebase_factory import FirebaseFactory
from lib.src.core.factories.flask.flask_factory import FlaskFactory

AppInjections.registerBinds()
FirebaseFactory.init()
app = FlaskFactory.init()

if __name__ == "__main__":
    app.run()
