# --- python imports
from functools import wraps
from tornado.gen import coroutine

# --- app module imports
from loc_app.helpers.utils import posted
from loc_app.helpers.users import current
from loc_app.helpers.errors import InvalidUsage
from loc_app.database.database import database_read_one


def expects(fields):

    def _validate(handler_func):
        
        @wraps(handler_func)
        @coroutine
        def _wrapper(self, *args, **kwargs):

            data = posted(self)
            if not data:
                raise InvalidUsage(reason='Missing required data field/s: {0}'.format(', '.join(fields)), status_code=400)
                
            if set(fields) - set(data.keys()):
                missing_fields = list(set(fields) - set(data.keys()))
                raise InvalidUsage(reason='Missing required data field/s: {0}'.format(', '.join(missing_fields)), status_code=400)

            yield handler_func(self, *args, **kwargs)

        return _wrapper

    return _validate


def authenticate_user(handler_func):

    @wraps(handler_func)
    @coroutine
    def _wrapper(self, *args, **kwargs):

        user = yield current(self)
        if not user:
            raise InvalidUsage(reason='Invalid or expired token.', status_code=401)

        yield handler_func(self, *args, **kwargs)

    return _wrapper


