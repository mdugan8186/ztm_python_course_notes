# ==== useful modules 2 ====

# for the array section at the bottom
from array import array


# == datetime ==
import datetime


# time - we can create time objects
print(datetime.time(5, 45, 2))
# 05:45:02


# date - gives the date object
print(datetime.date.today())


# == time ==
# from time import time
# this can be seen with the performance decorator we built
# time - takes an instance of time

# def performance(func):
#     def wrapper(*args, **kwargs):
#         # this will see what the start time is
#         time1 = time()
#         result = func(*args, **kwargs)
#         # this will see what the end time is
#         time2 = time()
#         print(f'It took {time2 - time1} s')
#         return result
#     return wrapper


# == array ==
# lists in python are called dynamic, anytime we need data into a list we cam make it as big as we want, we can incrementally increase the list and fill up our memory
# arrays that python gives us actually take up less memory and perform faster
# if you have a large list that you don't want to use generators for you can improve it with an array. this is because when we create an array we can set how much memory we can use in our machine

# with array you need to give it a typecode. typecodes with an array is what type of data is this array going to hold. this is part of the optimization. by telling it what type of data we're going to hold the memory is better used. you can find the typecode in the VScode tooltip or on python documentation on modules
arr = array('i', [1, 2, 3])
print(arr)
# we can access it just like a normal list/ array
print(arr[0])

# arrays are more performant than lists.
# this is a quick easy way to optimize your code if you don't want to use generators and you have a massive list
