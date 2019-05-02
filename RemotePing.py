from robotremoteserver import RobotRemoteServer

class RemotePing(object):

    def pong(self, name):
        return "pingo"+name

if __name__ == "__main__":
    RobotRemoteServer(RemotePing())