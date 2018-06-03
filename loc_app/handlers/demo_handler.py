from tornado.web import RequestHandler
from tornado.gen import coroutine

# --- app module imports


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		self.write('Hello World!\n')
