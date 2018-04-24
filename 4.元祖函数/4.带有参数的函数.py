# 定义函数
def sum_2_nums(a, b):
    print(a+b)


# 调用函数
sum_2_nums(1, 2)


def get_wendu():
    wendu = 20
    print('当前温度为%d'%wendu)
    return wendu

def get_wendu_huashi(wendu):
    wendu = wendu + 20
    print('获取的华氏温度为%d'%wendu)
    return wendu

result = get_wendu()

print(result)

print(get_wendu_huashi(result))


# 函数的多个返回值

def test():
    a = 11
    b = 22
    c = 33

    return [a, b, c]
    return (a, b, c)
    return a, b, c