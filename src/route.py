# pylint: disable=W0702, W0719

from flask import Blueprint, jsonify, request
from .auth_jwt import token_instance, token_verify

route_blueprint = Blueprint("route", __name__)

@route_blueprint.route("/secret", methods=["GET"])
@token_verify
def get_secret_message(token):
    """Mensagem Secreta
    :desc - Precisamos de alguma informação (token) 
            de acesso para esta rota ao mesmo tempo que
            é necessário criar essa informação que será 
            utilizada.  Através desse sistema protegemos
            a mensagem.
    """

    mensagem = {
        'segredo' : 'casco de tartaruga',
        'token' : token
    }
    return jsonify({ 'data' : mensagem }), 200


@route_blueprint.route("/auth", methods=["POST"])
def authorization_route():
    """Rota de geração do token
    :desc - Os tokens podem ser gerados e utilizados de 
            diversas maneiras, como cookies, 
            pelo jwt, etc.
    """

    try:
        body = request.get_json()
        user_id = body['user_id']

        if not user_id or not isinstance(user_id, int):
            raise Exception
    except:
        return jsonify({ 'error' : "Cannot identify request user's id" }), 400

    token = token_instance.create(user_id=int(user_id))
    return jsonify(
        { 'token' : token }
    ), 201
