# ==== higher order functions ====

# HOC (higher order function)
# can be one of two things.
# 1. a function that accepts another function inside of its parameters
def greet(func):
    func()

# 2. a functions that returns another function


def greet2():
    def func():
        return 5
    return func


# an example of a higher order function is the map(), filter(), and reduce() function because they accepts another function as a parameter
