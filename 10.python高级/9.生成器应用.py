
def test():

    i = 0

    while i < 5:

        temp = yield i

        print(temp)
        i += 1

a = test()

print(next(a))

a.send('hehe')

print(next(a))

a.send('haha')
