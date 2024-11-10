# ==== decorators 2 ====

# a decorator supercharges our function, it's simply a function that wraps another function and enhances it

# this is the syntax for a decorator
# notice that when we return the other function we aren't calling it, we are just returning so later on someone can use it
# def my_decorator(func):
#     def wrap_func():
#         func()
#     return wrap_func


def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func


# this is a simple function
def hello():
    print('hello')


# as soon as we write an @ python knows this is going tho be a decorator. as long as we follow the syntax of accepting a function as a parameter, having a wrapper function, calling the function, and returning the wrapper function
# when using a decorator it will be used on top when defining our function
@my_decorator
def bye():
    print('see ya later')

# what we did with the decorator hasn't changed anything. the function works exactly as expected, but what it allows us to do is that now we can add extra functionality. decorators are a function that wraps another function and enhances it


hello()
bye()


# under the hood all we're doing is this
def hello2():
    print('hello again')


# variable a = hello2 and wrapping this hello2 and calling it with my_decorator
a = my_decorator(hello2)
# then we're calling a
a()

# this is the same as
my_decorator(hello2)()


# the reason decorators are useful is that instead of running functions like in the last two examples and looking confusing we can just add the @decorator over the function and then we don't need to do what we did in the last two examples because they will be automatically wrapped by the @decorator
