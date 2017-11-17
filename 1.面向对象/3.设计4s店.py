class CarStore(object):

    def __init__(self):
        self.factory = Factory();

    def order(self,car_type):
        car =  self.factory.select_car_by_type(car_type)
        return car

class Factory(object):
    #通过类型选择车辆
    def select_car_by_type(self,car_type):
        return Car()

class Car(object):

    def start(self):
        print("开启发动机")
    def music(self):
        print("开始听音乐")
    def stop(self):
        print("车停下了")

car_store = CarStore()
car = car_store.order("vw")
if car:
    car.start()
    car.music()
    car.stop()
