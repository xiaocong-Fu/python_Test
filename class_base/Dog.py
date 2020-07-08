class dog():
# 因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
# 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def __init__(self,name,*age):                                                # __init__（self）此方法必须要有，用于给类中变量赋值
        self.name = name                                                        # 以self为前缀的变量都可供类中的所有方法使用
        self.age = age[0]                                                          # 可以通过实例访问类中的变量称为----属性
    def sit(self):
        print(self.name + ' is now sitting!!!!')
    def roll_over(self):
        print(str(self.age)+ ' is rolled over!!!!')

# 创建实例
my_dog = dog('haha',6)
print(my_dog.name + ' is my dog age is ' + str(my_dog.age))
# 调用方法
my_dog.sit()
my_dog.roll_over()
you_dog = dog('yaya',15)                                                           # 跟使用任意数量的实参方式一样

# 使用类和实例






