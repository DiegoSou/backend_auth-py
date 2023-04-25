from functools import wraps
import jwt
from flask import jsonify, request
from src.auth_jwt.token_handler import token_instance
from src.config.jwt_config_file import jwt_config

def token_verify(function: callable) -> callable:
    """Decorador de verificação do token"""

    @wraps(function)
    def decorated(*args, **kwargs):
        """Precisa da verificação do token"""

        head_encoded_token = request.headers.get("Authorization")
        head_user_id = request.headers.get("user_id")

        if not head_encoded_token or not head_user_id:
            return jsonify({ 'error' : "Cannot identify request user's id" }), 400

        token = head_encoded_token.split()[1]

        try:
            token_informations = jwt.decode(
                jwt=token,
                key=jwt_config['TOKEN_KEY'],
                algorithms='HS256'
            )
            
            token_user_id = token_informations['uid']

        except jwt.exceptions.InvalidSignatureError:
            return jsonify({ 'error' : "Token inválido" }), 401
        except jwt.exceptions.ExpiredSignatureError:
            return jsonify({ 'error' : "Token expirado" }), 408
        except KeyError:
            return jsonify({ 'error' : "Token inválido" }), 400

        if int(token_user_id) != int(head_user_id):
            return jsonify({ 'error' : "Usuário inválido" }), 401

        new_token = token_instance.refresh(token)

        return function(new_token, *args, **kwargs)

    return decorated
    