import os
from dotenv import load_dotenv
load_dotenv()

jwt_config = {
    "TOKEN_KEY" : os.getenv("TOKEN_KEY"),
    "MIN_EXPIRATION_TIME" : int(os.getenv("MIN_EXPIRATION_TIME")),
    "MIN_REFRESH_TIME" : int(os.getenv("MIN_REFRESH_TIME"))
}
