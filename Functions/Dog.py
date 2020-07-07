class dog():
# 因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
# 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def __init__(self,name,age):
        self.name = name                                                        # 以self为前缀的变量都可供类中的所有方法使用
        self.age = age
    def sit(self):
        print(self.name + ' is now sitting!!!!')
    def roll_over(self):
        print(self.age + ' is rolled over!!!!')
