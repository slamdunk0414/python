
#range(x,y,z) 从x到y 包括x不包括y z为步长 默认为1
#range(x) 从0到x 包括0不包括x

#类似于切片 [x:y:z] 从x到y 步长为z
for i in range(10,78):
    print(i)


#range的风险 可能范围太大内存异常（python3不会）


#列表生成式
a = [i for i in range(1,18)]
#执行for i in range(1,18) 循环 将值添加到列表里面

#生成式带判断

b = [i for i in range(10) if i %2 == 0]

print(b)
