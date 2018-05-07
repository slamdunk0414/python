
class Test():

    def __init__(self,func):
        self.__func = func

    def __call__(self):
        print('装饰器中的功能')
        self.__func()

@Test
def test():
    print('test')

test()