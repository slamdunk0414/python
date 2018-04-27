ori_file_name = '123.txt'
f1 = open(ori_file_name,'r')

str = f1.read()

position =  ori_file_name.rfind('.')
file_name = ori_file_name[0:position] + '[复件]' + ori_file_name[position:]

f2 = open(file_name,'w')

f2.write(str)

f1.close()
f2.close()