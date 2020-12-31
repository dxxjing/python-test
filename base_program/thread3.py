#!/usr/bin/python3

import time
import threading  # 推荐使用

# 线程同步
# 同步的效果是 一个线程 一旦拿到锁就会一直执行到结束,即使遇到io操作也不会让出执行权,所以打印出来的线程编号不会是错乱的
threadLock = threading.Lock()
threads = []


class myThread(threading.Thread):

    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.thread_name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.thread_name, self.counter)
        # 释放锁，开启下一个线程
        threadLock.release()


# 线程执行函数
def print_time(thread_name, counter):
    while counter:
        time.sleep(2)
        print("%s: %s, num=>%d" % (thread_name, time.ctime(time.time()), counter))
        counter -= 1


# 创建线程
t1 = myThread(1, 'thread-1', 3)
t2 = myThread(2, 'thread-2', 3)
t3 = myThread(3, 'thread-3', 3)

# 等待5s并发执行
time.sleep(3)
# 启动线程
t1.start()
t2.start()
t3.start()
# 添加线程到 线程列表
threads.append(t1)
threads.append(t2)
threads.append(t3)
# 阻塞等待回收线程
for t in threads:
    t.join()

print("主线程退出")
