
def test1():
    print('test1')
    test2()

def test2():
    print('test2')

test1()

def input_num():
    return int(input('请输入一个数字'))

def add():
    total = 0
    num1 = input_num()
    num2 = input_num()
    num3 = input_num()
    total = num1 + num2 + num3
    print(total)

add()