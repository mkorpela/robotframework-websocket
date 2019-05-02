from websocket import create_connection

class RfBound(object):

    def ping(self, name):
        return "pongi"+name

if __name__ == "__main__":
    data = "ping"
    while data.startswith("ping"):
        ws = create_connection("ws://localhost:8000/")
        data = ws.recv()
        ws.send(RfBound().ping(data.split(":")[1]))
        ws.close()