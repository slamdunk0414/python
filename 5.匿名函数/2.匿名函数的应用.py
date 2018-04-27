
def test(a,b):
    result = a+b
    return result

num = test(11,22)
print(num)

def test2(a,b,func):
    result = func(a,b)
    return result

num = test2(11,22,lambda x,y:x*y)
print(num)

#如果在python3中想通过输入获取匿名函数 需要

func_new = input('请输入一个匿名函数')

func_new = eval(func_new)

num2 = test2(11,22,func_new)
print(num2)

