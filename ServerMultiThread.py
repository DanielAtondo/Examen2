import socket
import os
from _thread import *
from telnetlib import SE
from threading import Thread

ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5001
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print("Server Started and socket is listening...")
ServerSideSocket.listen(1)

def multi_threaded_client(conn):
    #conn.send(str.encode("Welcome to the server"))
    while True:
        data = conn.recv(1024)
        print('received {!r}'.format(data))
        if data:
                print('sending data back to the client')
                conn.sendall(data)
        else:
            print('no data from', address)
            break
    conn.close()# Printing a message to the console.
    
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()