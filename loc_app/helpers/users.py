# --- python imports
import uuid
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import *


@coroutine
def create_user(phone_number):

    user = yield database_read_one('user', {'phone_number': phone_number})
    if not user:
        user = {
            'id' : '{0}'.format(uuid.uuid4()),
            'phone_number' : phone_number,
            'token' : '',
            'location' : {},
            'username' : '',
            'mobile_verified' : False
        }

        yield database_insert_one('user', user)
    
    return user
