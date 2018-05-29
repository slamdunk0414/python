
from greenlet import greenlet
import time

def f1():

    while True:

        print('f1')
        time.sleep(1)
        gr2.switch()


def f2():
    while True:
        print('f2')
        time.sleep(1)
        gr1.switch()


gr1 = greenlet(f1)
gr2 = greenlet(f2)

gr1.switch()