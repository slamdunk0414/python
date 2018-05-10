from threading import Thread,Lock

g_num = 0;

def test():
    global g_num


    for i in range(1000000):
        mutex.acquire()
        g_num += 1;
        mutex.release()
    print(g_num)

def test2():
    global g_num

    for i in range(1000000):
        mutex.acquire()
        g_num += 1;
        mutex.release()
    print(g_num)


#创建互斥锁
mutex = Lock()

t1 = Thread(target=test)
t2 = Thread(target=test2)

t1.start()
t2.start()