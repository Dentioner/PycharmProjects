#coding:utf-8
class car:
    speed = 0
    def calculate(self, distance):
        time = distance/self.speed
        print('It will take %.2f to arrive at the target')%time

print('小小行程计算器v1.0')
auto = car()
a = raw_input('你的速度为（两位小数）：')
b = raw_input('你的路程为（两位小数）：')
speed = float(a)
distance = float(b)
auto.speed = speed
auto.calculate(distance)
print('好了')
