#!/usr/bin/python3

import multiprocessing

a = 1


def demo1():
    global a
    a += 1


def demo2():
    # 打印出来的值是2 说明是共享的 线程是共享
    # 打印结果是1 进程是不共享的
    print(a)


def main():
    t1 = multiprocessing.Process(target=demo1)
    t2 = multiprocessing.Process(target=demo2)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
