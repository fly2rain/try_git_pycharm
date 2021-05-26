from line_profiler import LineProfiler
import random


def do_one_stuff(numbers):
    l = [numbers[i]/43 for i in range(len(numbers))]


def do_other_stuff(numbers):
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]


def do_stuff(numbers):
    for i in range(3):
        print(i)
        s = sum(numbers)
        do_one_stuff(numbers)
        do_other_stuff(numbers)


if __name__=='__main__':
    numbers = [random.randint(1,100) for i in range(1000)]
    lp = LineProfiler()
    lp.add_function(do_one_stuff)
    lp.add_function(do_other_stuff)
    lp_wrapper = lp(do_stuff)
    lp_wrapper(numbers)
    lp.print_stats()