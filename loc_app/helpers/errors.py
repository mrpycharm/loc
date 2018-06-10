# --- python imports
from tornado.web import HTTPError

class InvalidUsage(HTTPError):
    pass
