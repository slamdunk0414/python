
def test(num):

    def test_in(num2):

        print('num is %d'%(num + num2))

    return test_in;

ret = test(100)

ret(200)