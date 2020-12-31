#!/usr/bin/python3

# 类的继承 （单继承）

class base:
    # 定义公有属性
    name = ''
    age = 0

    # 定义私有属性
    __addr = ''

    # 构造方法
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr

    def say(self):
        print("%s, %d, %s" % (self.name, self.age, self.__addr))


class child(base):
    grad = 0

    def __init__(self, name, age, addr, grad):
        base.__init__(self, name, age, addr)
        self.grad = grad

    # 重写父类say方法
    def say(self):
        print("%s, %d, %d" % (self.name, self.age, self.grad))


c = child('tom', 11, 'shanghai', 4)
c.say()  # 调用子类中的方法 此时父类同名方法被覆盖
super(child, c).say()   # 用子类对象调用父类同名方法
