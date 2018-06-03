from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import database_insert_one, database_update, database_delete


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		yield database_delete('user', {'name' : 'Abdullah'})
		self.write('Hello World!\n')
