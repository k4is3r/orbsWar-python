import socket
import _pickle as pickle

class Network:
    """
    class to connect, send and recive information from server
    need to hardcode the host attribute to be the server's ip
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #the host ip addrees
        self.host = "192.168.1.12"
        #the connection port 
        self.port = 5555
        self.addr = (self.host, self.port)
        