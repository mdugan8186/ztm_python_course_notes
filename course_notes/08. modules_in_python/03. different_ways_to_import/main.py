# ==== different ways to import ====

# 6.
# it is recommended to use import *
# it is saying from the utility module import everything. that way if we get an error we will have to go to the file and see what is causing the error. an example would be a name error
from utility import *


# 3./ 5.a
# we can use the new syntax to import multiple functions also
# a reason we would want to import individual functions is to prevent name collision. this is if we had a function with the same name as another function or a built in function. we would be overriding an existing function and giving us a totally different function now
# import utility
# from utility import multiply, divide  # , max


# 1.
# we can have another package inside of a package (called a subpackage). the way to access this is to use the folder name, use dot notation for the other folder, then use dot notation for the module.
# the problem with this is that is getting long, ugly.
# import shopping.more_shopping.shopping_cart

# print(shopping.more_shopping.shopping_cart.buy('apple'))


# 2.
# a better way to import is to use this syntax
# use from then the packages and folders with dot notation, followed by import, and then the function we want to use
# this way is much cleaner
# from shopping.more_shopping.shopping_cart import buy


# 4.
# another good way is to import the entire module instead of just individual functions
# this is the best method to use to prevent name collision. instead of having multiple functions that ca be overridden we only have one name space
from shopping.more_shopping import shopping_cart
# 4.a
# to access it the syntax would be the module with dot notation to access the function
print(shopping_cart.buy('apple'))


# 3.a
# you can simply use the function like it was part of the main.py file without using all the dot notation
# print(buy('apple'))

print(divide(5, 2))
print(multiply(5, 2))


# 5.
# example for the name collision
# it will throw a TypeError
# print(max([1, 2, 3]))


# 7.
# it is recommended to be explicit and say exactly what you want to import. the format usually follows the:
# import statement followed by the package.module or import the module
# import package.module
# import module

# or

# from package.subpackage import module
# from module import function/ functions
