#!/usr/bin/python3

# list 列表 一个列表可以包含任意类型
# 索引值以 0 为开始值，-1 为从末尾的开始位置。

list1 = [1, 'test', 1.2, True]
tinyList = [4, 'tiny']
print(list1)    # [1, 'test', 1.2, True]

# 截取
print(list1[0])
print(list1[:])
print(list1[0:])
print(list1[0:2])
print(list1 + tinyList)     # 拼接
print(tinyList * 2)     # 连续输出
print(list1[0:-1:2])    # 第三个参数表步长 与string一致
'''
1
[1, 'test', 1.2, True]
[1, 'test', 1.2, True]
[1, 'test']
[1, 'test', 1.2, True, 4, 'tiny']
[4, 'tiny', 4, 'tiny']
[1, 1.2]
'''

# 与string 不同的是 list内的元素是可以改变的
list1[0] = 111
print(list1)    # [111, 'test', 1.2, True]

print(list1[-1::-1])    # 从末尾开始截取且步长为-1 用于反转列表 [True, 1.2, 'test', 111]

