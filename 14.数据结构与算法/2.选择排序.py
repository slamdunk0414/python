
''' 选择排序的逻辑

列表从头开始取 取出最小的 放到列表最左边
    再从头+1位置开始取 循环 知道取完

'''

list = [10,58,64,1,79,88,114,53,24,13]

n = len(list)

for i in range(n-1):
    minIndex = i
    for j in range(i,n):
        if (list[j] < list[minIndex]):
            minIndex = j
    list[i],list[minIndex] = list[minIndex],list[i]
    print('替换后的list为%s'%list)





