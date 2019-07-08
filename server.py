import socket
import _thread
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Server started. Waiting for connection")

def threadedConnection(conn):
    pass

while True:
    conn, addr = s.accept()
    print("Connected to: " + addr)
    