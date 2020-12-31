#!/usr/bin/python3

import sys


# 生成器 使yield的函数 并返回迭代器

def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a, b = b, a + b
        count += 1


it = fibonacci(10)  # 生成迭代器

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
