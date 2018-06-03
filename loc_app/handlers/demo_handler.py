from tornado.web import RequestHandler
from tornado.gen import coroutine, sleep


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		self.write('Hello World!\n')
