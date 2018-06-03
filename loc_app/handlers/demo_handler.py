from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import database_read_one


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		database_read_one('user')
		self.write('Hello World!\n')
