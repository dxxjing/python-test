#!/usr/bin/python3


# 数据类型

counter = 100
miles = 1000.0
name = 'hello python3'

print(counter)
print(miles)
print(name)
'''
100
1000.0
hello python3
'''

# 多变量赋值

a = b = c = 1
x, y, z = 1, 2, 'hello'
print(a, b, c, x, y, z)

# Number 数字
n1, n2, n3 = 1, 1.1, True
print(type(n1), type(n2), type(n3))
# <class 'int'> <class 'float'> <class 'bool'>

val = 1
print(val)
# 删除变量
del val
# 删除多个变量
# del val1, val2,...

# 运算
n1, n2 = 5, 4
print(n1 + n2)  # 9
print(n1 - n2)  # 1
print(n1 * n2)  # 20
print(n1 / n2)  # 1.25 除法得到一个浮点数
print(n1 // n2)  # 1 除法得到一个整数
print(n1 % n2)  # 1 取余
print(n1 ** n2)  # 625 乘方
print(2 + 3.1)  # 5.1 混合运算中 python 会将整型转化为浮点型

# 一个变量可通过赋值 指向不同的数据类型
va = 1.1
print(va)
va = 'string'
print(va)

