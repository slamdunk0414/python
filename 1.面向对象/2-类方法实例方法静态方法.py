class Game(object):

    num = 0;

    def __init__(self):
        self.score = 1

    #类方法
    @classmethod
    def add_num(cls,score):
        cls.num += score

    #静态方法
    @staticmethod
    def print_menu():
        print("就是打印 谁都能用")

Game.add_num(123)
#类方法可以用类名调用 还能通过实例调用
game = Game()
game.add_num(1233)

print(Game.num)

game.print_menu()
Game.print_menu()
