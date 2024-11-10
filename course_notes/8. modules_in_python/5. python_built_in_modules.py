# ==== python built in modules ====

# the core language of python is pretty small, this keeps things simple. python is useful through  external modules and packages. python has an entire package system were we can barrow and expand on the python functionality. these are called python built in modules. all the modules were installed when we downloaded the python interpreter, it comes with python, but in order for us to use them we have to import them. in other languages the built in modules would be called a standard library.


# this will import random
import random

print(random)
# <module 'random' from '/usr/lib/python3.12/random.py'>

# to learn more about a module we can use the help() function that comes with python
# to escape help press the 'q' key for quite
# help(random)

# another thing we can use to learn about a module is to use the dir() function. this will show all the methods available on this package
# print(dir(random))


# random has a random method
# this will give us a random number between 0 and 1
print(random.random())

# randint()
# this takes 2 parameters. where it should start and where it should end. it will then give you a random integer in that range
print(random.randint(1, 10))

# choice()
# this will have 1 parameter, an iterator list and it will randomly pick one from the list we give it
print(random.choice([1, 2, 3, 4, 5]))

# shuffle()
# shuffle returns None and has the sequence inplace (it modifies whatever list we're giving it in place)
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


# another way to import a random method is this:
# from random import shuffle


# we can also give random an alias
# import random as stuff

# now we would use stuff in place of random
# stuff.randint(1,10)

# this is to avoid name collisions


# it is good practice is to always import only what you need. this is explicit and shows what function is being imported and used so there is no guessing involved
# example
# from random import shuffle
