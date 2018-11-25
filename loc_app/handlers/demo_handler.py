from tornado.gen import coroutine
from tornado.web import RequestHandler

# --- app module imports
from loc_app.handlers.base_handler import BaseHandler
from loc_app.errors.base_errors import InvalidUsage


class MainHandler(BaseHandler):
    @coroutine
    def get(self):
        # self.write("Hola World!")
        raise InvalidUsage(reason="Noting", status_code=500)