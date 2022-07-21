"""Flask config."""
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


AUTH0_CLIENT_ID = 'AUTH0_CLIENT_ID'
AUTH0_CLIENT_SECRET = 'AUTH0_CLIENT_SECRET'
AUTH0_CALLBACK_URL = 'AUTH0_CALLBACK_URL'
AUTH0_DOMAIN = 'AUTH0_DOMAIN'
AUTH0_AUDIENCE = 'AUTH0_AUDIENCE'
PROFILE_KEY = 'profile'
SECRET_KEY = 'ThisIsTheSecretKey'
JWT_PAYLOAD = 'jwt_payload'

class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")

    AUTH0_CALLBACK_URL = environ.get(AUTH0_CALLBACK_URL)
    AUTH0_CLIENT_ID = environ.get(AUTH0_CLIENT_ID)
    AUTH0_CLIENT_SECRET = environ.get(AUTH0_CLIENT_SECRET)
    AUTH0_DOMAIN = environ.get(AUTH0_DOMAIN)
    AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
    AUTH0_AUDIENCE = environ.get(AUTH0_AUDIENCE)