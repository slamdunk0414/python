class Dog(object):
    #单例对象
    __instance = None
    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        
a = Dog()
b = Dog()

print(id(a))
print(id(b))
