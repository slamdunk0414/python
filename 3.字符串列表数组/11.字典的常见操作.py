
info = {'name':'zp','age':123,'height':1.73}

print(info.keys())

for key in info.keys():
    print(key)

for item in info.items():
    print('key = %s value = %s'%(item[0],item[1]))