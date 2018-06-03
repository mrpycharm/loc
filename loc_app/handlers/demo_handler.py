from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import database_insert_one


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		yield database_insert_one('user', {'name' : 'ahmed'})
		self.write('Hello World!\n')
