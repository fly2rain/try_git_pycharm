# cf. https://www.liujiangblog.com/course/python/79
import time
import threading

"""
#################################################
# Case1: 多线程使用方法 1: 🔥 继承Thread类，并重写它的 run() 方法
#################################################
"""
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__(name=thread_name)

    def run(self):  # 🍎 需要跑的程序在这个 run() 里面
        print(f"{self.name} - fyzhu - 正在运行中 ...\n")


class Case1:
    @staticmethod
    def call_thread():
        for i in range(5):
            MyThread("thread-" + str(i)).start()


"""
#################################################
# Case2: 方法 2: 实例化 threading.Thread 对象的时候，将线程要执行的任务函数作为参数传入线程
#################################################
"""
class Case2:
    @staticmethod
    def show(arg):
        time.sleep(1)
        print('thread ' + str(arg) + " running....")

    @staticmethod
    def call_thread():
        for i in range(5):
            # 🔥 target 是线程函数 (*可调用对象*), args=(i,) 是 target 函数的输入参数
            t = threading.Thread(target=Case2.show, args=(i,))
            t.start()


"""
#################################################
# Case3: 在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务，比如下面的例子
    - Python 默认会等待最后一个线程执行完毕后才退出 (`daemon`默认是 False, 是前台陈鳄龟须)。
    - 下面例子中，主线程没有等待子线程t执行完毕，而是啥都不管，继续往下执行它自己的代码,
        - 执行完毕后也没有结束整个程序，而是等待子线程 t 执行完毕，整个程序才结束。
#################################################
"""
class Case3:
    @staticmethod
    def doWaiting():
        print('start waiting:', time.strftime('%H:%M:%S'))
        time.sleep(3)
        print('stop waiting', time.strftime('%H:%M:%S'))

    @staticmethod
    def call_thread():
        t = threading.Thread(target=Case3.doWaiting)
        t.start()

        # 确保线程 t 已经启动
        time.sleep(1)
        print('start job')  # 🔥, 主程序的代码反而运行的比 thread (doWaiting) 运行的快
        print('end job')


"""
#################################################
# Case4: 有时候我们希望主线程等等子线程，不要“埋头往前跑”。那要怎么办？使用`join()`方法
#################################################
"""
class Case4:
    @staticmethod
    def call_thread():
        t = threading.Thread(target=Case3.doWaiting)
        t.start()

        # 确保线程 t 已经启动
        time.sleep(1)
        print('start join')
        # 🔥🔥 将一直堵塞，直到t运行结束。
        t.join()
        print('end join')


"""
#################################################
# Case5: 自定义线程类
-   对于threading模块中的Thread类，本质上是执行了它的run方法。
-   因此可以自定义线程类，让它继承Thread类，然后重写run方法。
#################################################
"""
class MyThreading(threading.Thread):

    def __init__(self, func, *args):
        super(MyThreading, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)  # 🔥


class Case5:
    @staticmethod
    def my_func(args):
        """
        你可以把任何你想让线程做的事定义在这里
        """
        pass

    @staticmethod
    def call_thread():
        obj = MyThreading(Case5.my_func, 123)
        obj.start()


"""
#################################################
# Case6: 线程锁
-   什么是 "线程不安全"?
    -   由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了
    -   当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。
-   怎样保证数据安全?
    -   为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据.
    -   线程锁用于锁定资源.
    -   可以同时使用多个锁，当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。
#################################################
"""

""" 1. 没有线程锁, 结果并不等于 2,000,000，可以很明显地看出脏数据的情况.
- 这是因为两个线程在运行过程中，CPU随机调度，你算一会我算一会，在没有对number进行保护的情况下，就发生了数据错误。
- 如果想获得正确结果，可以使用join()方法，让多线程变成顺序执行
"""
class Case6:
    num = 0  # class static variable, 模拟公共变量

    @staticmethod
    def plus():
        for _ in range(100000):  # 进行一个大数级别的循环加一运算
            Case6.num += 1
        print(f"子程序 {threading.current_thread().getName()} 运行结束后, num = {Case6.num}")

    @staticmethod
    def call_thread():
        for i in range(2):  # 用2个子线程，就可以观察到脏数据
            t = threading.Thread(target=Case6.plus)
            t.start()

        time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算
        print(f"主程序执行完毕后, num={Case6.num}")


""" Case7 使用 join() 方法，让多线程变成顺序执行
    - 为了防止脏数据而使用 join()的方法，其实是让多线程变成了单线程，属于因噎废食的做法.
    - 正确的做法是使用线程锁。Python在 threading 模块中定义了几种线程锁类.
        - Lock 互斥锁
        - RLock 可重入锁
        - Semaphore 信号
        - Event 事件
        - Condition 条件
        - Barrier “阻碍”
"""
class Case7:
    num = 0
    @staticmethod
    def plus():
        for _ in range(100000):  # 进行一个大数级别的循环加一运算
            Case7.num += 1
        print(f"子程序 {threading.current_thread().getName()} 运行结束后, num = {Case7.num}")

    @staticmethod
    def call_thread():
        for i in range(2):  # 用2个子线程，就可以观察到脏数据
            t = threading.Thread(target=Case7.plus)
            t.start()
            t.join()   # 🔥🔥🔥🔥 加了 join(), 让每个 thread 按照顺序运行.

        time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算
        print(f"主程序执行完毕后, num={Case7.num}")


""" Case8: 互斥锁`Lock`
    - 互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。
    - 使用很简单，初始化锁对象，然后将**锁当做参数传递给任务函数**，在*任务中加锁*，*使用后释放锁*。
"""
class Case8:
    num = 0

    @staticmethod
    def plus1(lk):
        lk.acquire()        # 🔥🔥开始加锁
        for _ in range(100000):  # 进行一个大数级别的循环加一运算
            Case8.num += 1
        print(f"子程序 {threading.current_thread().getName()} 运行结束后, num = {Case8.num}")
        lk.release()        # 🔥🔥释放锁，让别的线程也可以访问number

    @staticmethod
    def plus2(lk):
        with lk:            # 🔥🔥🔥 通过 with lk 定义 lock 代码范围
            for _ in range(100000):  # 进行一个大数级别的循环加一运算
                Case8.num += 1
            print(f"子程序 {threading.current_thread().getName()} 运行结束后, num = {Case8.num}")

    @staticmethod
    def call_thread():
        lock = threading.Lock()   # 🔥🔥🔥 定义 lock
        # for i in range(2):      # 用2个子线程，就可以观察到脏数据
        threading.Thread(target=Case8.plus1, args=(lock,)).start()  # 需要把锁当做参数传递给plus函数
        threading.Thread(target=Case8.plus2, args=(lock,)).start()  # 需要把锁当做参数传递给plus函数

        time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
        print(f"主程序执行完毕后, num={Case8.num}")


""" Case9: RLock
 """
class Case9:
    num = 0

    @staticmethod
    def run(lock):
        while True:
            lock.acquire()
            print(f"{threading.current_thread().getName()} locked,  num={Case9.num}")
            if Case9.num >= 2:
                lock.release()
                print(f"{threading.current_thread().getName()} released,  num={Case9.num}")
                break
            Case9.num += 1
            print(f"{threading.current_thread().getName()} released,  num={Case9.num}")
            lock.release()

    @staticmethod
    def call_thread():
        lock = threading.RLock()
        t1 = threading.Thread(target=Case9.run, name="A-worker", args=(lock,))
        t2 = threading.Thread(target=Case9.run, name="B-worker", args=(lock,))
        t1.start()
        t2.start()


if __name__ == '__main__':
    # Case4.call_thread()

    # Case5.call_thread()
    # Case6.call_thread()
    # Case7.call_thread()
    Case8.call_thread()
    # Case9.call_thread()