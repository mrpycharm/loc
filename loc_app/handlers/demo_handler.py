from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports
from loc_app.database.database import database_insert_many


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		data = [
			{'name' : 'hadi'},
			{'name' : 'rana'}
		]
		yield database_insert_many('user', data)
		self.write('Hello World!\n')
