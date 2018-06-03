# --- python imports
import motor, urllib
import tornado.ioloop
from tornado.web import Application
from tornado.httpserver import HTTPServer

# --- app module import
from handlers.demo_handler import MainHandler
from loc_app.config.db_config import DB_USER, DB_PASS, DB_URL, DB_DB


if __name__ == '__main__':
    
    # generate a motor client
    client = motor.motor_tornado.MotorClient('mongodb://' + DB_USER + ':' + urllib.quote(DB_PASS) + '@' + DB_URL + '/' + DB_DB)

    # get the db
    db = client[DB_DB]

    app = Application([
        (r'/', MainHandler),
    ])

    server = HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()