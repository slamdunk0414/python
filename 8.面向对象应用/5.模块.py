#两种倒入方法

import time

from time import *

#倒入模块 会把模块内的方法都执行 需要在倒入的模块中进行判断

#__name__只有在内部执行时 是__main__ 被其它调用 会显示为文件名
if __name__ == '__main__':
    xxx
