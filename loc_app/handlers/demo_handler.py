from tornado.gen import coroutine
from tornado.web import RequestHandler

# --- app module imports
from loc_app.handlers.base_handler import BaseHandler
from loc_app.helpers.errors import InvalidUsage


class MainHandler(BaseHandler):
    @coroutine
    def get(self):
        raise InvalidUsage(reason='Nothing', status_code=400)
            
