
#定义一个类

class Tank:
    #属性

    #方法需要添加self
    def fire(self):
        print('开火')

    def go(self):
        print('走')

t = Tank()
t.fire()
t.go()