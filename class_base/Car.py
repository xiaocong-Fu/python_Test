# car类中修改属性值
class car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0                                       # 属性指定默认值

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it !!!!!')

    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer')

    def increment_odometer(self,mileage):                               # 3.通过创建方法对属性的值进行递增
        self.odometer_reading += mileage

# my_new_car = car('benci','X6',2019)
# my_new_car.odometer_reading = 50                                        # 1.直接赋予属性值
# my_new_car.update_odometer(100)                                          # 2.通过方法修改属性的值
# my_new_car.update_odometer(500)
# my_new_car.increment_odometer(900)
# my_new_car.read_odometer()

# -------------------------------------------继承-----------------------------------------
import Grammar
# Grammar.path.append('D:\pythonCharm\Test\Test02\BaseTest\Grammar.py')
class ElectricCar(car):                                                 # 创建子类时，父类必须包含在当前文件中，且位于子类前面，定义子类时，括号内必须制定父类名称
    def __init__(self,make,model,year,color):
        super().__init__(make,model,year)                               # super()是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar的父类的方法__init__()，
                                                                        # 让ElectricCar实例包含父类的所有属性。#
        # self.battery_size = Grammar.Battery().battery_size            # （1）将Grammar.Battery类中的值赋予ElectricCar类中的值,这种赋值不适合调用ElectricCar类中其他的属性和数值
        self.battery_size = Grammar.Battery(100)                         # （2）将Grammar.Battery实例化赋予ElectricCar类中的属性
        self.color = color

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kwh battery')

    def get_descriptive_name(self):                                     # 重写父类的方法
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model + '\n\tit is a ' + self.color + ' car'
        return long_name

my_tesla = ElectricCar('tesla','model s',2020,'black')
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()                                           # （1）使用ElectricCar类中的方法输出
my_tesla.battery_size.describe_battery()                              # （2）使用Grammar.Battery类中的方法输出
my_tesla.battery_size.get_range()