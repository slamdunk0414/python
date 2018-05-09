import os
import time

#fork创建一个新的进程
ret = os.fork()

if ret == 0 :
    print('子进程')
    print('--%s--%s' % (os.getpid(), os.getppid()))
else:
    print('父进程')
    print('--%s--' % os.getpid())