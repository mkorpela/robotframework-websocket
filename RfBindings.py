import subprocess
import time
from websocket import create_connection

class RfBindings(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, name, attrs):
        self._process = subprocess.Popen(["python", __file__])
        time.sleep(0.1)

    def _end_suite(self, name, attrs):
        self._process.kill()

    def get_keyword_names(self):
        return ['ping']

    def run_keyword(self, name, args, kwargs):
        ws = create_connection("ws://localhost:8000/")
        ws.send(name+":"+args[0])
        result = ws.recv()
        ws.close()
        return result


if __name__ == "__main__":
    from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

    clients = []
    class SimpleServ(WebSocket):

        def handleMessage(self):
          for client in clients:
            if client != self and not client.closed:
                client.sendMessage(self.data)
            
        def handleConnected(self):
            clients.append(self)

        def handleClose(self):
            clients.remove(self)
    
    server = SimpleWebSocketServer('', 8000, SimpleServ)
    server.serveforever()