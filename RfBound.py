from websocket import create_connection

class RfBound(object):

    def ping(self):
        return "pongi"

if __name__ == "__main__":
    data = "ping"
    while data == "ping":
        ws = create_connection("ws://localhost:8000/")
        data = ws.recv()
        ws.send(RfBound().ping())
        ws.close()