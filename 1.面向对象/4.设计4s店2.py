#工厂方法
#创建父类 不实现方法 让子类实现

class Store(object):
    def select_car(self,car_type):
        pass
    def order(self,car_type):
        return self.select_car(car_type)

class Factory(object):
    def select_car_by_type(self,car_type):
        pass

class BMWFactory(Factory):
    def select_car_by_type(self,car_type):
        print("收到订单%s"%(car_type))
        return car_type

class BMWStore(Store):
    def select_car(self,car_type):
        self.car = BMWFactory().select_car_by_type(car_type)

bmwStore = BMWStore();
bmw = bmwStore.order("3x")
