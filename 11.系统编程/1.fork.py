import os
import time

#fork创建一个新的进程
ret = os.fork()

if ret == 0 :
    while True:
        print('1')
        time.sleep(1)
else:
    while True:
        print('2')
        time.sleep(1)