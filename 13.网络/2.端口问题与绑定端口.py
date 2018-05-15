
#每次发送 端口都不一致 需要绑定端口

from socket import  *

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',7788))

addr = ('172.16.10.128',8081)

b = bytes('keke\n',encoding='utf8')

s.sendto(b,addr)

data = s.recvfrom(1024)
print(data)
#地址信息
print(data[1])
s.close()

#单工：只能往一个方向 类似收音机

#半双工：互抢频道

#全双工：电话