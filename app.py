import tornado.ioloop
from tornado.web import Application
from tornado.httpserver import HTTPServer

# --- app module import
from stocks.handlers.demo_handler import MainHandler
from stocks.handlers.user_handler import UserHandler


if __name__ == '__main__':

    app = Application([
        (r'/', MainHandler),
        (r'/ws', UserHandler),
    ])

    server = HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
