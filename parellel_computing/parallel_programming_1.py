#!/usr/bin/env python3
""" Code for https://www.linkedin.com/learning/python-parallel-and-concurrent-programming-part-1/multiple-threads-python-demo?u=26192810 """
import os
import threading


""" C20: 演示一个简单的 thread 例子, 显示 pid, threading.active_count() 和返回 Thread 对象列表
"""
class C2_0:
    # a simple function that wastes CPU cycles forever
    @staticmethod
    def cpu_waster():
        while True:
            pass

    @staticmethod
    def start_n_waster_thread(n=12):
        print(f'\nStarting {n} CPU Wasters...')
        for i in range(n):
            threading.Thread(target=C2_0.cpu_waster).start()

    @staticmethod
    def display_mp_thread_info():
        print('\n  Process ID: ', os.getpid())  # 🔥🔥 os.getpid() 信息, process 的信息.
        print('Thread Count: ', threading.active_count())
        for thread in threading.enumerate():  # 🔥 返回当前活动 Thread 对象列表
            print(thread)

    @staticmethod
    def call_thread():
        C2_0.display_mp_thread_info()  # 1. display information about this process
        C2_0.start_n_waster_thread(12)  # 2. start 12 CPU threads
        C2_0.display_mp_thread_info()  # 3. display information about this process


""" C2_1: 演示简单的 multiprocessing 例子
"""
import multiprocessing as mp

class C2_1:
    @staticmethod
    def start_n_waster_mp(n=12):
        print(f'\nStarting {n} CPU Wasters...')
        for i in range(n):
            mp.Process(target=C2_0.cpu_waster).start()  # 🔥🔥 start a process. 和 thread 类似.

    @staticmethod
    def call_mp():
        C2_0.display_mp_thread_info()
        C2_1.start_n_waster_mp(12)
        C2_0.display_mp_thread_info()


if __name__ == '__main__':
    # C2_0.call_thread()
    C2_1.call_mp()