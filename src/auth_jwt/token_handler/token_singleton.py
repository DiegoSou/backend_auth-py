from src.config.jwt_config_file import jwt_config
from .token_creator import TokenCreator

token_instance = TokenCreator(
    token_key=jwt_config['TOKEN_KEY'],
    min_exp_time=jwt_config['MIN_EXPIRATION_TIME'],
    min_refresh_time=jwt_config['MIN_REFRESH_TIME']
)
