from multiprocessing import Process
import time

def test():
    for i in range(5):
        print(i)
        time.sleep(1)

p = Process(target=test)
p.start()

#添加join 会等子进程执行完会运行
p.join()

print('--main--')