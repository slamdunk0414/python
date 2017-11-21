#为了防止别人导入的时候 引入无用方法
#将想让别人导入的方法名放到__all__里面
#如果别人导入的时候 使用 from all import *的方式 就不能使用__all__外的方法与变量、类

__all__ = ["test1"]

def test1():
    print("------test1------")

def test2():
    print("------test2------")
