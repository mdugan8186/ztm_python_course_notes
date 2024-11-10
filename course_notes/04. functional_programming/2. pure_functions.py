# ==== pure functions ====

# what is a pure function?
# instead of a box we had before of objects of all these functionalities, instead think of it as a simple function.
# if we give it input, something will happen to the input that every time results in the same thing

# a pure functions has 2 rules
# 1) given the same input it will always return the same output
# 2) a function should not produce any side effects. side effects are things that a function does that effects the outside world. an example would be if you were to print something inside of a function it effects the outside world because you're printing something onto a screen, the screen is the outside world. or the function was touching a variable that lived outside of a different scope.

# this is an example of a pure function because it does the same thing every time and doesn't touch the outside world
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))


# this is not a pure function because it effects the outside world by printing inn the display, causing side effects
def multiply_by3(li):
    new_list = []
    for item in li:
        new_list.append(item * 3)
    print(new_list)


multiply_by3([1, 2, 3])


# this is not a pure function because it has side effects. it effects something outside of its scope
new_list = []


def multiply_by4(li):
    for item in li:
        new_list.append(item * 4)
    return new_list


print(multiply_by4([1, 2, 3]))


# when you have pure functions you'll have less buggy code, you'll be able to test your code better, it's easier to understand your code, and overall you have these benefits of not having different parts of your code touching each other and effecting each other, which makes your life as a programmer so much easier

# pure functions is more of a guideline than an absolute, it is impossible to have pure functions everywhere because if a function doesn't effect the outside world at all we wouldn't have any programs, we wouldn't be able to display anything, or save things. it's impossible to have pure functions everywhere, however when you can wherever you can functional programming teaches us that pure functions are good. try to create pure functions and only have few non pure functions that maybe interact with the outside world that we can go back to whenever we have bugs in our code because most likely those are the ones that are going to have bugs than pure functions

# to finalize our concept of functional programming well use the example of our Wizard from the OOP section

wizard = {
    'name': 'Merlin',
    'power': 50,
}

# instead of containing theses in a class we would have different methods, wouldn't be a method it would be a function because it doesn't live inside of a class


def attack():
    pass


# in functional programming they say we don't need to combine data with functions, let's keep those separated, let's create pure functions that can be passed anything. this way keep those two things separate so that we can focus on pure functions and we can focus on data. at the end of the day it's all about trying to keep our code clean and avoiding bugs in our code
