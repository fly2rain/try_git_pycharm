#!/usr/bin/env python3
""" Threads that waste CPU cycles """

import os
import threading


# a simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass

def start_n_wasters(n=12):
    print('\nStarting 12 CPU Wasters...')
    for i in range(n):
        threading.Thread(target=cpu_waster).start()


def display_thread_info():
    print('\n  Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)


if __name__ == '__main__':
    # 1. display information about this process
    display_thread_info()

    # 2. start 12 CPU threads
    start_n_wasters(12)

    # 3. display information about this process
    display_thread_info()