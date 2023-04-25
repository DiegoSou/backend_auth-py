# pylint: disable=C0103

import time
from datetime import datetime, timedelta
import jwt

class TokenCreator:
    """Token Service Handler"""

    def __init__(self, token_key : str, min_exp_time : int, min_refresh_time : int):
        self.__TOKEN_KEY = token_key
        self.__MIN_EXPIRATION_TIME = min_exp_time
        self.__MIN_REFRESH_TIME = min_refresh_time

    def create(self, user_id : int):
        """Creates an encoded token"""
        return self.__encode_token(user_id)

    def refresh(self, encoded_token : str):
        """Refresh token"""

        token_information = jwt.decode(
            jwt=encoded_token,
            key=self.__TOKEN_KEY,
            algorithms='HS256'
        )

        token_uid = token_information['uid']
        exp_time = token_information['exp']

        if ((exp_time - time.time()) / 60) < self.__MIN_REFRESH_TIME:
            return self.__encode_token(token_uid)

        return encoded_token


    def __encode_token(self, user_id : int):
        """
        Criar token codificado
        :desc - Encode significa transformar uma informação de um tipo para
                outro tipo codificado, legível através de um elemento pivot
                A informação é transcrita de outro modo pelo encodamento
        """

        token = jwt.encode(
            {
                'exp' : datetime.utcnow() + timedelta(minutes=self.__MIN_EXPIRATION_TIME),
                'uid' : int(user_id)
            },
            key=self.__TOKEN_KEY,
            algorithm='HS256'
        )

        return token
