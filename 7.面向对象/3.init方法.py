#定义一个类

class Tank:
    #属性

    #方法需要添加self
    #初始化方法
    def __init__(self,new_name):
        self.name = new_name
        print('初始化姓名')

    #str方法 可以通过print方法 直接打印
    def __str__(self):
        return '我的名字是%s'%self.name

    def fire(self):
        print('开火')

    def go(self):
        print('走')

    def introduce(self):
        print('我的名字是%s'%self.name)

t = Tank('big tank')
t.fire()
t.go()

# t.name = 'big tank'

#获取属性的第一种方法
print(t.name)

#获取属性的第二种方法
t.introduce()

print(t)