#!/usr/bin/python3

# tuple 元组 也可以包含不同的数据类型
# 与list 区别 内部元素不能被更改
# 元组可以像 string  list 一样 截取
t1 = (1, 2.1, 'hello', True)

list1 = ['a', 'b']
t2 = (list1, '1', 2)

# t2[1] = '111' 元组内元素不可修改 但是包含可变变量时却可以修改该可变变量
# 将元组内第一个可变变量 list1 修改,修改会使原list也改变 所以元组内存储的是变量地址
t2[0][1] = 222
print(t2, list1)    # (['a', 222], '1', 2) ['a', 222]

num = 123
t3 = (num,) + t2
print(t3)
# t3[0] = 333 整形变量也不能修改 。。。
print(t3)

# 空元组
t4 = ()
# 元组内有一个元素 后面必须加逗号
t5 = (3,)

# 将list转化为tuple
list3 = [1, 2, 3]
print(tuple(list3))     # (1, 2, 3)
