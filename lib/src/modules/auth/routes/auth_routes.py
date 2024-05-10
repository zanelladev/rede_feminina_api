from flask import Blueprint, request

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    content = request.json
    # Faça o que você precisa com os dados do login
    return {"uuid": content['mytext']}, 200
