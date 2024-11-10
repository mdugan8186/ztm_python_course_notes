# ==== decorators ====

# decorators have the at(@) sign in front of them and then some sort of name
# @classmethod
# @staticmethod


# in python functions are what we call first class citizens, that is they ca be passed around like variables, they can be an argument inside of a function, they act just like variables

def hello():
    print('hello')


# with calling it in the variable
greet = hello()
print(greet)

# without calling it in the variable
greet2 = hello
print(greet2())

# this will delete the hello function (the name reference to the function that's in memory), however because greet and greet2 are a whole other variable and still is pointing to this function. python is going to delete the hello word however the greet and greet2 is still pointing in memory to this location so python is smart enough to say 'you told me to delete hello, i'll delete the name hello but i'm not going to delete the function because greet and greet2 is still pointing to it'
del hello
print(greet2())

# will cause a NameError
# hello()


# we can also pass functions around as arguments

def hello2(func):
    func()


def greetings():
    print('still here')


# we didn't have to call greetings function in here because the hello2 function calls it for us
a = hello2(greetings)

print(a)


# decorators are only possible because of the features, this ability of functions to act like variables, act like first class citizens in python. underneath the hood decorators are using this power of functions

# decorators supercharge our function. if we had our hello function by adding some sort of decorator we can supercharge our function and add extra functionality to it. it lets the python interpreter know i want this hello function  to have some extra features
