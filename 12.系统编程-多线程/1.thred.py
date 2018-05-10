from threading import Thread
import time

def test():
    print('睡一秒')
    time.sleep(1)

for i in range(5):
    t = Thread(target = test)
    t.start()

#第二种方法 创建一个Thread的子类

class MyThread(Thread):

    def run(self):
        print('run')

if __name__ == '__main__'
    t = MyThread()
    t.start()