#!/usr/bin/python3

import sys

# iter 迭代器
# 字符串 列表 或元组对象都可以创建迭代器

list1 = [1, 2, 3, 4]

it = iter(list1)  # 创建迭代器
print(next(it))  # 返回下一个元素 1
print(next(it))  # 返回下一个元素 2

# 使用for 遍历迭代器
for x in it:
    print(x, end='')    # 3 4

print()

# 使用while 遍历迭代器
list2 = list1
it2 = iter(list2)

while True:
    try:
        print(next(it2))
    except StopIteration:
        # break
        sys.exit()
