from flask import request, jsonify, Blueprint
from lib.src.modules.auth.domain.entities.user_entity import UserEntity


class AuthRoutes:
    blueprint = Blueprint("auth", __name__, url_prefix="/auth")

    users = [
        UserEntity('id1', 'email1', 'password1'),
        UserEntity('id2', 'email2', 'password2'),
        UserEntity('id3', 'email3', 'password3')
    ]

    @classmethod
    @blueprint.route("/login", methods=["POST"])
    def login(cls):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get("email", None)
        password = request.json.get("password", None)

        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400

        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        for user in cls.users:
            if user.email == username and user.password == password:
                return {"msg": "User login successfully."}, 200

        return {"msg": "User not found."}, 404

    @classmethod
    @blueprint.route("/register", methods=["POST"])
    def register(cls):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get("email", None)
        password = request.json.get("password", None)

        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400

        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        for user in cls.users:
            if user.email == username:
                return {"msg": "User already exists."}, 400

        new_user = UserEntity(str(len(cls.users) + 1), username, password)
        cls.users.append(new_user)

        return {"msg": "User registered successfully."}, 201
