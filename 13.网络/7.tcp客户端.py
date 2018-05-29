
import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('10.211.55.3',8899))
clientSocket.send('123'.encode('gb2312'))

msg = clientSocket.recv(1024)

print(msg)

clientSocket.close()