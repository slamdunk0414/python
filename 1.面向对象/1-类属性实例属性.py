class Tool(object):

    #定义一个类属性
    num = 0;

    def __init__(self,new_name):
        print("初始化对象%s"%(new_name))
        #对实例属性赋值
        self.name = new_name
        #对类属性赋值
        Tool.num += 1

t1 = Tool("1")
t2 = Tool("2")
t3 = Tool("3")

print(Tool.num)
