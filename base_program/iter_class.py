#!/usr/bin/python3

# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。

class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        # 最大调用20次 就抛出stop异常 结束迭代
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


num = MyNumbers()
it = iter(num)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
