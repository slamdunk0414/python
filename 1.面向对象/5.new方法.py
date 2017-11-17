class Dog():

    def __init__(self):
        print("init方法")

    def __del__(self):
        print("删除方法")

    def __str__(self):
        print("打印方法")
        return "self"

    def __new__(cls):
        print("new方法")

        #如果不返回 无法进行
        return super().__new__(cls)

dog = Dog()
