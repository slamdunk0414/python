
age = int(input("请输入年龄"))   #必须强制转换 不然没法跟18对比大小

if age > 18:
    print("大于18")
elif age > 15:
    print("大于15")
else:
    print("其他年龄")

