#args只能放在最后
def add_nums(*args):
    total = 0
    for num in args:
        total += num
    print('total is %d'%total)

#**kwargs 带变量名 会放入到kwargs中
def test(**kwargs):
    print(kwargs)

add_nums(11,22,33,44,55)

test(task = 11, done = 22)

def test2(*args,**kwargs):
    print(args)
    print(kwargs)

test2(11,22,33,name = 'zp' , height = 1.73)

#如果要向*args和**kwargs中传入已知的元祖和字典 需要加入*和**
#比如

A = (11,22,33)
b = {'name' : 'zp','height' : '1,73'}

test2(*A,**b)

#如果不加 则会变为一个元祖对象 添加到args中
