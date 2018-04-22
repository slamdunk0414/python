
# 列表

names = []  #python中可以放不同类型的数据

print(type(names))

# 列表的增删改查

# 增加
names.append('123')
print(names)

names.insert(0,'456')
print(names)

names2 = ['xxx','yyy','yyy','zzz','zzz']

names3 = names + names2

print(names3)

# extend 将目标数组添加进数组
names.extend(names2)
print(names)

# 删除
# pop 将最后一个删掉

names.pop()
print(names)

# remove 删除指定内容

names.remove('yyy')
print(names)

# del list[x] 输出列表中的指定位置的元素
del names[0]
print(names)

del names[-1]
print(names)

# 改变
# list[x] = 'xxx'

names[0] = 'hehe'
print(names)

# 查询
# in

if 'hehe' in names:
    print('hehe is in names')

