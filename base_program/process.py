#!/usr/bin/python3

from multiprocessing import Process
import os


# 创建子进程

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()   # 启动子进程
    p.join()    # 阻塞等待并回收子进程
    print('Child process end.')
