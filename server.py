import socket
import _thread
import sys

# Server contains the ip address
server = "192.168.0.102"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('', port))

except socket.error as e:
    str(e)

# Allow max of 2 clients
s.listen(2)
print("Server started. Waiting for connection")

pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    """
    Recieve data from client
    :param player: the current player we are dealing with
    :param conn: connection
    :return: None
    """

    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                reply = make_pos(pos[1 - player])

                print("Recieved: ", data)
                print("Sending: ", reply)

                conn.sendall(str.encode(reply))

        except socket.error as e:
            print(e)
            break
    print("Lost connection")
    conn.close()


def read_pos(pos):
    """
    Converts string data coming from server to tuple
    :param pos: string data
    :return: position tuple
    """
    pos = pos.split(',')
    return int(pos[0]), int(pos[1])


def make_pos(tup):
    """
    Converts tuple data from client to sendable server string
    :param tup: tuple data
    :return: string data
    """
    return str(tup[0]) + ',' + str(tup[1])


current_player = 0

while True:
    conn, addr = s.accept()    # Connect to a new client
    print("Connected to: ", addr)

    _thread.start_new_thread(threaded_client, (conn, current_player))    # Start new thread for the client

    current_player += 1
