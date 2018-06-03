from tornado.web import RequestHandler
from tornado.gen import coroutine, sleep


class MainHandler(RequestHandler):
	@coroutine
	def get(self):
		print('Request came in\n')
		yield sleep(5)
		print('writing reponse\n')
		self.write('Hello World!\n')
