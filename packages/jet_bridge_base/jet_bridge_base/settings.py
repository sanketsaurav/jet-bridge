import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CURRENT_MODULE = sys.modules[__name__]

BRIDGE_TYPE = ''
DEBUG = False
READ_ONLY = False
AUTO_OPEN_REGISTER = True

WEB_BASE_URL = None
API_BASE_URL = None

DATABASE_ENGINE = None
DATABASE_HOST = None
DATABASE_PORT = None
DATABASE_USER = None
DATABASE_PASSWORD = None
DATABASE_NAME = None
DATABASE_EXTRA = None
DATABASE_CONNECTIONS = None


def set_settings(settings):
    for key, value in settings.items():
        setattr(CURRENT_MODULE, key, value)
