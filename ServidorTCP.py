from http import client
from operator import index
import threading
import socket

host = ''
port = 5001

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nicknames=nicknames[index]
            broadcast(f'{nicknames} se ha desconectado'.encode('ascii'))
            nicknames.remove(nicknames)
            break
def receive():
    while True:
        client,address=server.accept()
        print(f'Conectado con {str(address)}')

        client.send('identificador'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        if nickname != 'Receptor':
            nickname='Emisor'
        nicknames.append(nickname)
        clients.append(client)

        print(f'El identificador del cliente es {nickname}')
        broadcast(f'{nickname} se ha conectado'.encode('ascii'))
        client.send('Conectado'.encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()
print('El servidor esta escuchando...')
receive()
