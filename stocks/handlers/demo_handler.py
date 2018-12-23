from tornado.gen import coroutine, sleep
from tornado.web import RequestHandler

# --- app module imports
from stocks.handlers.base_handler import BaseHandler
from stocks.errors.base_errors import InvalidUsage


class MainHandler(BaseHandler):
    @coroutine
    def get(self):
        # yield sleep(10)
        self.write("Hola World!")