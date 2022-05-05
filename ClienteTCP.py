from email import message
import socket
import threading
import serial

puertoCOM='COM5'
ipServidor='187.250.77.133'

serArduino = serial.Serial(puertoCOM, 9600)
nickname='Receptor'
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ipServidor,5001))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'identificador':
                client.send(nickname.encode('ascii'))
            else:
                if message == '0':
                    serArduino.write(b'0')
                else:
                    serArduino.write(b'1')
                print(message)
        except:
            print("Se ha desconectado")
            client.close()
            break
def write():
    while True:
        message=f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
