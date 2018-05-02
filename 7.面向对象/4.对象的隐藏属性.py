
class Dog:

    #__name 隐藏属性 无法直接修改
    def set_age(self,new_age):
        if(new_age >= 0):
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

d = Dog()
d.set_age(100)
print(d.get_age())
