
try:
    open('123.txt')
except Exception as result:
    print(result)
else:
    print('没有异常')
finally:
    print('不管怎么着 都会执行')