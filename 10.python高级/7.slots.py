
class Person():
    #限制属性
    __slots__ = ('name','age')

    def __init__(self):
        self.name = 'xx'
        self.age = 12

p = Person()
p.name = 'xxx'
p.addr = '123'

