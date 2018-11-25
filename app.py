import tornado.ioloop
from tornado.web import Application
from tornado.httpserver import HTTPServer

# --- app module import
from loc_app.handlers.demo_handler import MainHandler


if __name__ == '__main__':

    app = Application([
        (r'/', MainHandler),
    ])

    server = HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
