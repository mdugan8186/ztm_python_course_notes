# ==== packages in python ====

# a module is a python file
import utility2

# this is a package. a package is simply a folder. a package is a level up, it is a folder containing modules. you can have a package with multiple modules inside of it. the shopping_cart is a module while shopping is a package.
# when we import from a package we say the package name and use dot notation to access the module
import shopping.shopping_cart


print(shopping.shopping_cart.buy('apple'))


# when making packages it is important to create an __init__.py file. some IDEs create it automatically (like pycharm) (by clicking python package when creating a new folder). the interpreter will read the __init__ and know it is dealing with a python package. the file can be left completely empty


# whe running in pycharm if you run your code and get a message saying process finished with exit code zero. this means there are no errors. if you get a 1 it means there are errors
