
class Dog:

    __instance = None
    __init_flag = False

    def __new__(cls, name):

        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = super().__new__(cls)
            print('真正的创建')
            return cls.__instance

    def __init__(self,new_name):
        if Dog.__init_flag == False:
            self.name = new_name
            Dog.__init_flag = True


d = Dog('dd')
d2 = Dog('d2')

print(d.name)