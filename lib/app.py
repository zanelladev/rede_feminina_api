import uuid

from flask import request

from lib.src.core.flask.server import app
from lib.src.modules.auth.routes.auth_routes import auth_blueprint

app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run()
