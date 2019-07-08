import socket
import _thread
import sys

# Server contains the ip address
server = "192.168.0.102"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

# Allow max of 2 clients
s.listen(2)
print("Server started. Waiting for connection")

def threaded_client(conn):
    """
    Recieve data from client
    :param conn: connection
    :return: None
    """
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print('Disconnected')
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break


while True:
    conn, addr = s.accept()    # Connect to a new client
    print("Connected to: " + addr)

    _thread.start_new_thread(threaded_client, (conn,))    # Start new thread for the client
