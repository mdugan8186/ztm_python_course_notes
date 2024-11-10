# ==== why do we need decorators? ====

# practical applications of decorators we've seen are @classmethod and @staticmethod from classes

# a decorator we're going to create on  our own. it doesn't exist in python. this will be a performance decorator we can use during testing our code  to see how fast our code runs

# modules will be talked about later, but we are importing from the time module something called time
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        # this will see what the start time is
        time1 = time()
        result = func(*args, **kwargs)
        # this will see what the end time is
        time2 = time()
        print(f'It took {time2 - time1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i * 5


long_time()


# now we have a decorator that we can give to pretty much any function in our program and actually measure the performance of our function, which is very useful.
# now can test how performant our code is before we deploy our code or put the code out into the world to see if we can optimize things in different ways
# the performance decorator will depend on the machine and how fast your cpu and memory are on your computer. the code we ran may take more or less time depending on your machine, this is a nice way to compare functions relatively

# decorators are used a lot in python libraries and frameworks, web frameworks like Django and Flask, maybe you want an authentication decorator where each function can only be run if the user is authenticated (like having the privilege to run a function like logging_in to a website), or a login or logging decorator that just logs and lets your database know that someone has logged into your system or someone has purchased something from Amazon, or someone just requested a friend request
