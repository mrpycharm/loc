# --- python imports
from tornado.gen import coroutine

# --- app module imports
from loc_app import db


@coroutine
def database_read_one(collection, read_filter={}):
    print db