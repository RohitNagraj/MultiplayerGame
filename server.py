import socket
import _thread
import pickle

from player import Player

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

# List to hold player class objects
players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]


def threaded_client(conn, player):
    """
    Recieve data from client
    :param player: the current player we are dealing with
    :param conn: connection
    :return: None
    """

    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # Receive state of this thread's player
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                # Send state of the other player
                reply = players[1 - player]

                print("Recieved: ", data)
                print("Sending: ", reply)

                conn.sendall(pickle.dumps(reply))

        except socket.error as e:
            print(e)
            break
    print("Lost connection")
    conn.close()


current_player = 0

while True:
    conn, addr = s.accept()    # Connect to a new client
    print("Connected to: ", addr)

    _thread.start_new_thread(threaded_client, (conn, current_player))    # Start new thread for the client

    current_player += 1
