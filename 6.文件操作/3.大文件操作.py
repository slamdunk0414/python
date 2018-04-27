
# read()操作会读出所有内容
#
# readline()会一行一行读
#
# readlines()会把所有读出来 放到数组里

f = open('123.txt','rb')

f.seek(2,0)

str = f.readline()
print(str)

f.seek(2,2)

str = f.readline()

print(str)