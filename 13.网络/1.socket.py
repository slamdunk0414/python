from socket import  *

s = socket(AF_INET,SOCK_DGRAM)
addr = ('172.16.10.128',8081)

b = bytes('你好',encoding='utf8')

s.sendto(b,addr)

s.close()