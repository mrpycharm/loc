import tornado.ioloop
from tornado.web import Application
from handlers.demo_handler import MainHandler


def make_app():
    return Application([
	(r'/', MainHandler),
    ])



if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
