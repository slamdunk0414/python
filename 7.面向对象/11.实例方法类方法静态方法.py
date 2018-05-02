class Game:

    #类属性
    num = 0

    def __init__(self):

        #实例属性
        self.name = 'game'

    #类方法
    @classmethod
    def add_num(cls):
        cls.num += 1

    #静态方法
    @staticmethod
    def print_menu():
        print('123')


Game.add_num()
print(Game.num)

#如何调用静态方法
#通过类和对象都可以

Game.print_menu()

g = Game()
g.print_menu()