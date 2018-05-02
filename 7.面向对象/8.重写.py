
class Dog:

    def bark(self):
        print('汪汪叫')

class XTQ(Dog):

    def bark(self):
        print('狂叫')

        #第一种方式
        Dog.bark(self)

        #第二种方式
        super().bark()

x = XTQ()
x.bark()