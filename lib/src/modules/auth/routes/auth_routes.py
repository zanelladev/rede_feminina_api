from flask import request, jsonify, Blueprint
from lib.src.core.flask.server import app
from lib.src.modules.auth.domain.entities.user_entity import UserEntity

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

users = [
    UserEntity('id1', 'email1', 'password1'),
    UserEntity('id2', 'email2', 'password2'),
    UserEntity('id3', 'email3', 'password3')
]


@auth_blueprint.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("email", None)
    password = request.json.get("password", None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    for user in users:
        if user.email == username and user.password == password:
            return {"msg": "User login successfully."}, 200

    return {"msg": "User not found."}, 404
