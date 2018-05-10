from threading import Thread

g_num = 0;

def test():
    global g_num
    for i in range(1000000):
        g_num += 1;
    print(g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1;
    print(g_num)

t1 = Thread(target=test)
t2 = Thread(target=test2)

t1.start()
t2.start()