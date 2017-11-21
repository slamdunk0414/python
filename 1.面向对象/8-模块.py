#模块就是py文件

#模块的导入
#第一种方法
import sys

#第二种方法
from sys import argv

'''判断 如果__name__ == '__main__'
        则证明是自己类调用
        如果不是
        则证明是其它类导入自己调用
'''
if __name__ == '__main__':
    main()
