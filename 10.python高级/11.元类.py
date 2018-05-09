#
# #type为元类 用于创建类
# #()内为父类 {}内为属性
# Test2 = type("Test2",(),{})
#
# t2 = Test2()
#
# print(type(t2))


class Dog:

    def eat(self):
        print('eat')

d1 = Dog()

eat = d1.eat

eat()

