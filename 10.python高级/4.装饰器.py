# #第一种写法
# def w1(func):
#
#     def yz():
#         print('验证')
#         func()
#     return yz
#
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#
# f1 = w1(f1)
# f1()


#第二种写法
# def w1(func):
#
#     def yz():
#         print('验证')
#         func()
#     return yz
# @w1
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#
# f1()

#3 带参数的装饰器
# def w1(func):
#
#     def yz(a,b):
#         print('验证')
#         func(a,b)
#     return yz
# @w1
# def f1(a,b):
#     print('f1')
#     print('a = %d b = %d'%(a,b))
#
# def f2():
#     print('f2')
#
# f1(11,22)

#4 装饰器对有返回值的函数的装饰
# def w1(func):
#
#     def yz(a,b):
#         print('验证')
#         c = func(a,b)
#         return c
#     return yz
# @w1
# def f1(a,b):
#     print('f1')
#     print('a = %d b = %d'%(a,b))
#     c = a + b
#     return c
#
# def f2():
#     print('f2')
#
# c = f1(11,22)
# print(c)

#带有参数的装饰器
def func_arg(arg):
    def func(func_name):
        def func_in():
           print('闭包里面的内容')
           print(arg)
           func_name()
        return func_in
    return func
@func_arg('xxx')
def f1():
    print('f1')

f1()