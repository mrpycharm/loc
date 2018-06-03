import tornado.ioloop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from handlers.demo_handler import MainHandler


def make_app():
    return Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    server = HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()