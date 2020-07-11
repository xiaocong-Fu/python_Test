# ---------------------------------------------导入类----------------------------------------
from Car import car                                         # 有标红，但是实际是可以运行         导入单个类
my_new_car = car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 导入多个类： from 模块名 import 类名1，类名2
# 到如整个模块： import 模块名            不会与当前文件使用的任何名称发生冲突
# 导入模块中所有的类：from 模块名 import *
# 在一个模块中导入另一个模块  ：from 模块名 import 类名
