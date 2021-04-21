import threading
import time

number = 0
lock = threading.Lock()


def plus(lk):
    global number  # global声明此处的number是外面的全局变量number
    lk.acquire()  # 开始加锁
    for _ in range(1000000):  # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    lk.release()  # 释放锁，让别的线程也可以访问number


if __name__ == '__main__':
    for i in range(2):  # 用2个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus, args=(lock,))  # 🔥🔥需要把锁当做参数传递给plus函数,注意传递对象🔥🔥🔥
        t.start()
    time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)
