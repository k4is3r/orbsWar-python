import socket
import _pickle as pickle

class Network:
    """ 
    class to connect, send and recieve information from the server
    need to hardcode the host attribute to be server's ip
    """

    def __int__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.settimeout(10.0)
        #this ip is going to hardcode to connect
        self.host = "192.168.1.12"
        self.port = 5555
        self.addr = (self.host, self.port)

    def connect(self, name):
        """ 
        connects to server and returns the id of the client that connected
        name: str
        return: int representing id
        """
        self.client.connect(self.addr)
        self.client.send(str.encode(name))
        val = self.client.recv(8)
        return int(val.decode())

    def disconnect(self):
        """ 
        disconnects from the server
        return: None
        """
        self.client.close()
    
    def send(self, data, pick=False):
        """ 
        sends information to the server
        data: str
        pick: boolean if should pickle or not
        return : str
        """
        try:
            if pick:
                self.client.send(pickle.dumps(data))
            else:
                self.client.send(str.encode(data))
            reply = self.client.recv(2048*4)
            try:
                reply = pickle.loads(reply)
            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)