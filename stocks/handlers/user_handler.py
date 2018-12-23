# --- python module imports
from tornado.websocket import WebSocketHandler
from tornado.gen import sleep


class UserHandler(WebSocketHandler):
    """
        Handles all the incoming websocket connections
    """

    def check_origin(self, origin):
        """
            Need to implement this method in order to secure the websockets.
            For now just returning True will work but for the sake of security
            we need to implement proper origin checks in the method.
        """
        print 'Origin: ' + origin
        return True

    def on_message(self, message):
        print 'Message: ' + str(message)

    def on_close(self):
        print 'closing connection'
