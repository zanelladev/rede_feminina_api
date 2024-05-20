from flask import request, jsonify, Blueprint
from lib.src.core.services.injector.injector import Injector
from lib.src.modules.auth.domain.entities.user_entity import UserEntity
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRoutes:

    blueprint = Blueprint("auth", __name__, url_prefix="/auth")

    @classmethod
    @blueprint.route("/login", methods=["POST"])
    def login():
        auth_repository = Injector.retrieve(IAuthRepository)

        auth_repository.signIn()

        users = [
            UserEntity('id1', 'email1', 'password1', 'name1', 'surname1'),
            UserEntity('id2', 'email2', 'password2', 'name2', 'surname2'),
            UserEntity('id3', 'email3', 'password3', 'name3', 'surname3')
        ]

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

    @classmethod
    @blueprint.route("/signup", methods=["POST"])
    async def register():
        try:
            auth_repository = Injector.retrieve(IAuthRepository)
            await auth_repository.signUp()

            return {"msg": "User not found."}, 200

        except Exception as e:
            return jsonify({
                "msg": "An error occurred while trying to sign up the user.",
                "error": str(e)
            }), 400
