
import socket

udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ('172.16.10.255',8081)

udpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

udpSocket.sendto(b'123',addr)

udpSocket.close()