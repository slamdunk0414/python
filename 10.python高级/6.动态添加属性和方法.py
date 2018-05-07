
import types

class P():

    def eat(self):
        print('吃')


def run(self):
    print('跑')

p1 = P()

p1.eat()

p1.run = types.MethodType(run,p1)

p1.run()

