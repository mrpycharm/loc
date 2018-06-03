from tornado.web import RequestHandler
from tornad.gen import coroutine, sleep


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		yield sleep(5)
		self.write('Hello World!\n')
