from multiprocessing import Pool
import time
import os

def work(msg):
    print('%s start' % msg)
    time.sleep(1)
    print('%s end'%msg)
    print('pid %s'%os.getpid())

po = Pool(3)

for i in range(10):
    po.apply_async(work,(i,))


po.close()
po.join()

print('end')
