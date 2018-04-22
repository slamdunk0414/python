
info = {'name':'zp'}
print(info)

#写入没有的 即为增加
info['age'] = 18
print(info)

#删除 del

del info['age']
print(info)

#改 直接改

info['name'] = '123'
print(info)

info['xxx'] = '1234'

#查询 在不缺人是否有key的情况下 不要直接查询 如果不存在key会崩溃

str = info.get('xx')
print(str)

