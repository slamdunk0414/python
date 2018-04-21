
str = 'xxx yyy zzz xxx'

# find 如果找到 返回位置 没有则返回-1
print(str.find('zzz'))

print(str.find('ssss'))

# count 返回目标字符串出现的次数

print(str.count('xxx'))

print(str.count('zzz'))

# replace 替换目标字符串
# replace不会替换原始字符串 可以接受三个参数 1目标字符串 2替换后的字符串 3替换数量

str2 = str.replace('xxx','123')

print(str2)

# split 字符串切割

arr = str.split(' ')
print(arr)

# 判断开头和结尾  startwith endwith

a = str.startswith('xxx')

print(a)

b = str.endswith('123')

print(b)