
''' 选择排序的逻辑

先取一个元素
从元素后面开始 从右到左开始取 如果此元素比之前的元素大 则不用动
                         如果此元素比之前的小 则依次替换

'''

list = [58,10,64,1,79,88,114,53,24,13]

n = len(list)

for i in range(1,n):
    minIndex = i
    for j in range(i,0,-1):

        if (list[j] < list[j-1]):
            print('交换了 %d,%d'%(list[j],list[j-1]))
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break;


print(list)



