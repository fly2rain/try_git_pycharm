# from multiprocessing import Pool, cpu_count
import multiprocessing as mp


def f1(x):  # 🔥 假设给定一个 list, 函数对每个元素作操作.
    return x * x

def f2(x, y):
    return x + y


if __name__ == '__main__':
    print(f"num of cpu: {mp.cpu_count()}")
    with mp.Pool(5) as p:
        print(p.map(f1, [1, 2, 3]))  # 🔥 自动分配数据样本, 自动执行得到结果. 非常省事...

    with mp.Pool(3) as p:
        print(p.map(f2, [1, 2], 3))
