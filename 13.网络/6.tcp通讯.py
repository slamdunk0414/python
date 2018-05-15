
import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(('',7891))

print(serverSocket)

serverSocket.listen(10)

clientSocket,clientInfo = serverSocket.accept()

msg = clientSocket.recv(1024)

print("%s--%s"%(str(clientInfo),msg))