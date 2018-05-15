import socket
from threading import Thread

def main():
    def receiveMsg():

        while True:
            data = udpSocket.recvfrom(1024)
            if data:
                print(data[0].decode('gb2312'))
                udpSocket.sendto(b'msg_receive\n', data[1])

    def sendMsg():

        while True:
            str = input('<<')
            udpSocket.sendto(str.encode('gb2312'),('172.16.10.128',8081))

    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    udpSocket.bind(('',7789))

    t = Thread(target = receiveMsg)
    t.start()

    t2 = Thread(target = sendMsg)
    t2.start()

    t.join()
    t2.join()

if __name__ == '__main__':
    main()