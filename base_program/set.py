#!/usr/bin/python3

# set 集合
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# set 可包含不同数据类型
# set 是无序的

set1 = set('abcdedf')   # {'c', 'a', 'd', 'f', 'e', 'b'}
print(set1)

set2 = {'abc', 'bbb', 'ccc', 1, 'abc'}
# 输出会自动去除重复元素
print(set2)  # {1, 'ccc', 'bbb', 'abc'}

# 成员测试 验证成员是否在集合内
if 'a' in set2:
    print(True)
else:
    print(False)
# True


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素
