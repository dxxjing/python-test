#!/usr/bin/python3

import time
import _thread  # 已被弃用


# 线程

# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(("%s: %s, %d" % (thread_name, time.ctime(time.time()), count)))


# 创建线程
try:
    _thread.start_new_thread(print_time, ('thread-1', 2))
    _thread.start_new_thread(print_time, ('thread-2', 3))
except:
    print('Error: 无法启动线程')
while 1:
    pass
