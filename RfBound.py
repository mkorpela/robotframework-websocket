from websocket import create_connection

class RfBound(object):

    def ping(self):
        return "pong"

if __name__ == "__main__":
    print("HELLO YEAH")
    ws = create_connection("ws://localhost:8000/")
    data = ws.recv()
    if data == "ping":
        ws.send(RfBound().ping())
    ws.close()
    print("NOW IT IS OVER")