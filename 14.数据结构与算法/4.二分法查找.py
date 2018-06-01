
'''二分法只能从顺序表中使用

   list中找a

   先取中间元素b 如果取出来的结果比a大 则在b左边找
               如果取出来的结果比a小 则在b右边边找

               以此类推

'''

def binary_search(list,item):
    n = len(list)

    if n == 0 :
        return False

    mid = int (n / 2)

    if (list[mid] < item):

        print('中间的小')

        list = list[mid + 1:len(list)]
    elif (list[mid] > item):
        print('中间的大')
        list = list[0 : mid]
    else:
        print('正好找到')
        return True

    print(list)

    return binary_search(list,item)

list = [1,2,3,4,6,7,8,9]

b = binary_search(list,9)
print(b)
