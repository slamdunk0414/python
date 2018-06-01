
'''没啥好说的 从头开始取 找到比自己小的 替换位置'''

list = [1,5,4,6,7,8,99,0,5,6,7,3,45,2,34,123]

n = len(list)

for j in range(0,n-1):
    
    for i in range(0,n-1-j):
        
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
            print('替换了%d与%d'%(list[i],list[i+1]))
            
print(list)
        
    
    