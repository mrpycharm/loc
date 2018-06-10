# --- python imports
import json, uuid, hashlib
from tornado.gen import coroutine

# --- app module imports
from loc_app.config.app_config import LOGGING


def log(statment):
    if LOGGING:
        print(statment)


def posted(handler):
    data = {}
    try:
        data = json.loads(handler.request.body)
    except:
        pass

    return data


def hash_password(text):
    salt = '{0}'.format(uuid.uuid4())
    log(type(text))
    hashed_pass = hashlib.sha512((text + salt).encode('UTF-8')).hexdigest()

    return hashed_pass, salt
