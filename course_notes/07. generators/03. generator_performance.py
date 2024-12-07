# ==== generator performance ====

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result
    return wrapper


# proof that generators are more performant
# generator
@performance
def long_time():
    print('1')
    for i in range(1000000):
        i * 5


# list
@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i * 5


long_time()
long_time2()


# long_time is much faster and performant even though it does the same thing as ling_time2. it uses less recourses by not holding things in memory and process data efficiently
# generators are useful when calculating large sets of data, particularly if we're long loops  where we don't want to store that memory and we don't need to calculate everything at the same time, maybe just one by one

# a lot of libraries in python underneath the hood use generators instead of lists because they are so much faster


# generator syntax
def gen_fun(num):
    for i in range(num):
        yield i


for item in gen_fun(10):
    print(item)
