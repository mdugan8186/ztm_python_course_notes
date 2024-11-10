# ==== decorators 3 ====

# if we want to use an argument in our function

# this will throw a TypeError: my_decorator.<locals>.wrap_func() takes 0 positional arguments but 1 was given
# def my_decorator(func):
#     def wrap_func():
#         print('*********')
#         func()
#         print('*********')
#     return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)


# hello('hello')


# to get the argument to work we must add the parameter(param) to the wrapper function and the function it's calling
def my_decorator(func):
    def wrap_func(param):
        print('*********')
        func(param)
        print('*********')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('hello')


# it becomes complicated when we start adding multiple parameters and arguments. the solution to this is to use *args and **kwargs (*args takes all positional arguments and **kwargs takes all keyword arguments). this will unpack all the positional and keyword arguments

def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator2
def another_greeting(greeting, emoji=':('):
    print(greeting, emoji)


another_greeting('halo', ':)')
another_greeting('halo again')


# the reason they are called decorators is because they are a famous pattern in programming, called the decorator pattern

# this is the decorator pattern:
def my_decorator3(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func
