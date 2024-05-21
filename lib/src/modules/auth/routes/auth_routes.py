from flask import request, jsonify, Blueprint
from lib.src.core.exceptions.missing_json_exception import MissingJsonException
from lib.src.core.services.injector.injector import Injector
from lib.src.modules.auth.domain.exceptions.missing_email_exception import MissingEmailException
from lib.src.modules.auth.domain.exceptions.user_not_found_exception import UserNotFoundException
from lib.src.modules.auth.domain.repositories.i_auth_repository import IAuthRepository


class AuthRoutes:
    blueprint = Blueprint("auth", __name__, url_prefix="/auth")

    @classmethod
    @blueprint.route("/signin", methods=["POST"])
    async def signin():
        if not request.is_json:
            return MissingJsonException().toJson(), 400

        email = request.json.get("email", None)
        password = request.json.get("password", None)

        if not email:
            return MissingEmailException().toJson(), 400

        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        auth_repository = Injector.retrieve(IAuthRepository)

        await auth_repository.signIn()

        return jsonify(UserNotFoundException().toJson()), 404

    @classmethod
    @blueprint.route("/signup", methods=["POST"])
    async def signup():
        try:
            auth_repository = Injector.retrieve(IAuthRepository)
            await auth_repository.signUp()

            return {"msg": "User not found."}, 200

        except Exception as e:
            return jsonify({
                "msg": "An error occurred while trying to sign up the user.",
                "error": str(e)
            }), 400
