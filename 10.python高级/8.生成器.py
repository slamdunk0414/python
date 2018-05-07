
#列表生成式
a = [x for x in range(10)]

print(a)

#生成器 第一种方式
b = (x for x in range(10))

#是用next查看生成器里面的元素
print(next(b))

#生成器 第二种方式
def creatNum():
    a,b = 0,1
    print('开始生成')
    for x in range(5):
        yield  b
        a,b = b,a+b

creatNum()
#加入yield 会成为生成器 不会直接调用 需要是用next

a = creatNum()
next(a)

next会在yield处停止 再次调用yield会从yield处开始继续