# ==== reduce() ====

# this will be discussed more in the modules section
# this is importing something from functools. functools are what we call a tool belt that we can use for functional tools that comes with the python installation. from there there's a specific function we can import
# this is basically saying
# from tool belt import the reduce function
from functools import reduce


# reduce()
# The reduce() function is part of the functools module in Python and is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an iterable (like a list), reducing the iterable to a single value. It’s often used when you need to combine items of a sequence using a specified operation, like summing numbers, multiplying them, or merging data
# reduce(function, sequence(data), initial value)
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))  # 6

print(reduce(accumulator, my_list, 10))  # 16


# common ues cases for reduce() are:
# -Summing or multiplying a list of numbers.
# -Finding the maximum or minimum value in a sequence.
# -Flattening a list of lists.
