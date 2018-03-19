#coding:utf-8
class vehicle:
    def __init__(self,speed):
        self.speed = speed

    def calculate(self,distance):
        time = distance/self.speed
        print('It will take %f hours to arrive at target')%time

class bicycle(vehicle):
    pass
class car(vehicle):
    def __init__(self,speed,fuel):
        vehicle.__init__(self,speed)
        self.fuel = fuel
    def calculate(self,distance):
        vehicle.calculate(self,distance)
        totalfuel = distance*self.fuel
        print('It will cost around %f fuels')%totalfuel
print('小小行程计算器v2.0')
bike_speed = float(raw_input('自行车的速度为：'))
bike_distance = float(raw_input('自行车的行程为：'))
car_speed = float(raw_input('汽车的速度为：'))
car_distance = float(raw_input('汽车的行程为：'))
car_fuel = float(raw_input('汽车的油耗为：'))

bike = bicycle(bike_speed)
car = car(car_speed,car_fuel)
bike.calculate(bike_distance)
car.calculate(car_distance)

print('rua')
