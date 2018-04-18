
a = 100

b = 5.6

c = "123"

print('a的类型是%s'%type(a))

print('b的类型是%s'%type(b))

print('c的类型是%s'%type(c))

age = int(input("请输入年龄"))   #必须强制转换 不然没法跟18对比大小

if age > 18:
    print("成年了")
else:
    print("没成年")