# ==== generators 2 ====

# iterable is any object in python when we're able to loop through. underneath the hood it has the dunder iter method (__inter__) so when the object is created  this iter allows us to have an iterable object that can be iterated over

# iteration (to iterate something) is the act of taking an item from an iterable doing something to it then going on to then next one. when we use loop (for and while) we call that iteration. it's the process itself

# generators are actually iterable. that is everything that is a generator is iterable. you can iterate over them, but not everything that is iterable is a generator
# for example a range() is a generator, so that is always going to be iterable. a list is an iterable, but it's not a generator. so a generator is a subset of an iterable

# the difference between a generator and a regular iterable is the way we implement them


# define our own generator. generators are usually functions just like range is a function
# instead of returning like the function below we're going to use a keyword called yield. in this case we're going to yield the i
def generator_function(num):
    for i in range(num):
        yield i


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result

# instead of returning and appending the list and crating all this data we're going to use yield. yield pauses the function and comes back to it when we do something to it, which is called next. yield says says pause the function, yield i (give i) and when you tell me to keep going again then i'll keep going

# to do this
for item in generator_function(10):
    print(item)

# this is similar to the the make_list function but instead of having to create that list in memory it just kept going one by one, we only held one item in memory and we used it however we wanted to print(item) in our case


# yield - to return a list of values from a generator
# The yield keyword is used to return a list of values from a function.
# Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.
# When you call a function with yield keyword(s), the return value will be a list of values, one for each yield.


# if used return we would just get a value, but with yield
def generator_function2(num):
    for i in range(num):
        yield i * 2


g = generator_function2(10)
print(g)  # generator object
next(g)  # 0
next(g)  # 2
print(next(g))  # 4

# yield pauses the function and comes back to it when next() is called. so if it has a yield keyword i becomes a generator, it keeps track of this state of the value and it only keeps the most recent data in memory

# if we run next past the number given we'll get a StopIteration error. next can be called as many times as we want until the range expires. when we exceed the number of items in the range we'll get an error


# next()
# returns the next item in an iterable
# The next() function returns the next item in an iterator.
# You can add a default return value, to return if the iterator has reached to its end.
# next(iterator, default)
