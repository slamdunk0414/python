#定义一个类

class Tank:
    #属性

    #方法需要添加self
    def fire(self):
        print('开火')

    def go(self):
        print('走')

    def introduce(self):
        print('我的名字是%s'%self.name)

t = Tank()
t.fire()
t.go()

t.name = 'big tank'

#获取属性的第一种方法
print(t.name)

#获取属性的第二种方法
t.introduce()
