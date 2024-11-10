# ==== how to debug code ====

# debugging is the act of removing (errors, bugs, or exceptions) from our program


# == tips for debugging code ==

# == linting ==
# linting allows us to detect as we code issues with our code before we even run our code

# num + 4
# the linter will detect that num is not defined


# == ide/ editor ==
# these (pycharm, VScode)have built in tools such as auto formatting based on pep8, detect errors with highlighting and formatting of our code


# == read errors ==
# read errors and understand what they mean
# num + 4 # throws a NameError
# 4 + 'stuff'  # throws a TypeError
# 4 + 'stuff throws a SyntaxError

# there are about 15 errors that are really common and show up ninety percent of the time. use the python documentation to learn about them


# == pdb (python debugger) ==
# pdb is a built on module in python
# it allows us to interact with the code

# = using print =
# def add(num1, num2):
#     # add a print statement to see whats going on
#     print(num1, num2)
#     return num1 + num2


# add(4, 'stuff')


# =using pdb =
import pdb


def add2(num1, num2):
    # add a set_trace()
    pdb.set_trace()
    # t = 4 * 5
    return num1 + num2


add2(4, 'stuff')

# the set_trace allows you to interact with you code from the terminal to help with debugging

# other useful features with the pdb once its active
# help - shows all the commands that you can use in the pdb
# list - shows the source code for the current file
# next - continues execution until the next line of code
# step - allows us to go the the next line of code after the pdb.set_trace()
# continue - allows us to continue through the code until something is returned
# a - gives all the current arguments of the current function we're in
# w - shows the context of the current line it is executing
# exit - exit the pdb
# q - quite the pdb

# once in the pdb we can change code from within it
