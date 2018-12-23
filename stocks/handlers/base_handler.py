# --- python imports
from tornado.web import RequestHandler
from tornado.gen import coroutine
import json


class BaseHandler(RequestHandler):
    ''' Base request to override few things like error messages e.t.c '''

    def write_error(self, status_code, **kwargs):
        
        message = self._reason
        if status_code == 500:
            message = 'Something went wrong.'
        
        error = {
            'status_code': status_code,
            'message': message
        }

        # call finish
        self.finish(json.dumps(error))
