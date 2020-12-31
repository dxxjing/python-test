#!/usr/bin/python3

import time
import threading  # 推荐使用

num = 0


class myThread(threading.Thread):

    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print('开始线程:' + self.thread_name)
        print_time(self.thread_name, self.counter, 5)
        print('线程结束：' + self.thread_name)


# 线程执行函数
def print_time(thread_name, delay, counter):
    while counter > 0:
        global num
        num += 1
        # time.sleep(delay)
        print("%s: %s, num=>%d" % (thread_name, time.ctime(time.time()), counter))
        counter -= 1


# 创建线程
t1 = myThread(1, 'thread-1', 1)
t2 = myThread(2, 'thread-2', 2)
t3 = myThread(3, 'thread-3', 3)

# 等待5s并发执行
time.sleep(5)
# 启动线程
t1.start()
t2.start()
t3.start()
# 阻塞等待回收线程
t1.join()
t2.join()
t3.join()

print("主线程退出", num)
