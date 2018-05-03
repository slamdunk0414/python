
class Car_store:

    def order(self,money):
        if money > 50000 :
            return Car()
        else:
            print('洗洗睡吧')

class Car:
    def move(self):
        print('车在动')

car_store = Car_store()

car = car_store.order(2100)


