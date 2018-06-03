from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import database_insert_one, database_update, database_delete


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		yield database_insert_one('user', {'name' : 'Ahmed'})
		yield database_update('user', {'name' : 'Ahmed'}, {'$set' : {'name' : 'Abdullah'}})
		yield database_delete('user', {'name' : 'Ahmed'})
		self.write('Hello World!\n')
