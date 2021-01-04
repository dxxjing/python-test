#!/usr/bin/python3

from multiprocessing import Pool
import os, time, random


# 进程池  由于进程池大小为4 但是却创建5个子进程，所以最后一个进程 只有等待前四个的其中一个结束 才会执行

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 调用join前必须调用close 调用close后不能再创建子进程
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
