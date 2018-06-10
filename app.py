import tornado.ioloop
from tornado.web import Application
from tornado.httpserver import HTTPServer

# --- app module import
from loc_app.handlers.demo_handler import MainHandler
from loc_app.handlers.user_handler import *


if __name__ == '__main__':

    app = Application([
        (r'/', MainHandler),\
        (r'/send_otp', GenerateOTPHandler),
        (r'/verify_otp', VerifyOTPHandler),
    ])

    server = HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
