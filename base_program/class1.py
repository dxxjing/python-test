#!/usr/bin/python3


class C1:
    num = 123

    def f(self):
        return "hello class:" + str(self.num)


c = C1()
print(c.num)
print(c.f())


class C2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


c2 = C2(1, 2)
print(c2.x, c2.y)


class C3:
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
        print("%s, %d, %s" %(self.name, self.age, self.__addr))


c3 = C3('jdx', 11, 'shanghai')
c3.say()
