
class Dog:
    def __new__(cls, *args, **kwargs):
        print('创建')
        return object.__new__(cls)

    def __init__(self):
        print('初始化')

d = Dog()
