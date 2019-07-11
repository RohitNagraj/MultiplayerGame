import socket
import pickle


class Network:

    """
    Connects a new client to the server and provides its network actions
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.102"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        """
        :return: the position of the client player
        """
        return self.p

    def connect(self):
        """
        Connects the client to the server
        :return: the data received from the server
        """
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def send(self, data):
        """
        Sends data from client to server and receives data from server
        :param data: data to send to server
        :return: data received from server
        """
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
