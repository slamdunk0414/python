class Tool(object):

    num = 0

    def __init__(self,new_name):
        self.name = new_name
        Tool.num += 1
        self.num2 = 0
        self.num2 += 2




t1 = Tool('t1')
t2 = Tool('t2')
t3 = Tool('t3')

print(Tool.num)

print(t1.num2)
print(t2.num2)
print(t3.num2)