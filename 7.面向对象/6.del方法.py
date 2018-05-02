import sys

class Dog:

    def __del__(self):
        print('删掉了')

d1 = Dog()
d2 = d1


print(sys.getrefcount(d1))

print('---1---')

del d1

print(sys.getrefcount(d2))

print('---2---')

del d2

print('---3---')
