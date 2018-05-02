class Base:
    def test(self):
        print('base')

class A(Base):
    def test(self):
        print('A')

class B(Base):
    def test(self):
        print('B')

class C(A,B):
    def test(self):
        print('C')

c = C()

#类名.__mro__ 决定了调用方法的顺序
print(C.__mro__)