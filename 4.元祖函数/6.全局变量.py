
wendu = 0
#建议用g开头新建全局变量 如g_wendu

list1 = [1,2,3]
#如果列表 字典当全局变量 不用加global

def print_wendu():
    global wendu
    wendu = 33
    list1.append(4)

def print_huashi_wendu():

    print(wendu)
    print(list1)

print_wendu()
print_huashi_wendu()