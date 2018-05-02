
class Dog:

    def __send_msg(self):
        print('正在发送')

    def send(self):
        self.__send_msg()

d = Dog()
d.send()