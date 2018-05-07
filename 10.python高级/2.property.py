
class Dog():

    def __init__(self):
        self.__age = 10

    def setAge(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            self.__age = 0

    def getAge(self):
        return self.__age

    age = property(getAge,setAge)

d = Dog()

d.age = -10
print(d.age)