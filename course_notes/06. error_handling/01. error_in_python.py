# ==== errors in python ====

# an unavoidable part of programming is that your programs are going to give a lot of errors, you can't avoid bugs or programs breaking


# this will throw an error
# print(1 + 'hello') # TypeError

# an error that crashes our program is called an 'exception'.

# python raises these exceptions whenever the interpreter says 'i have no idea what your doing, somethings wrong, i don't know i'm doing anymore, i'm going to stop whatever i'm doing and i'm going to give you an output'.

# error handling will handle these exceptions that will crash our program. a great programmer is able to handle errors in their program. instead of letting our programs error we're able to handle them
# error handling allows us to let the python script to continue running even if there are errors


# SyntaxError
# this is not standard python syntax, we have to fix the error
# def hello()
#     pass


# NameError
# raised when a variable does not exist or defined
# def hello():
#     1 + name
# hello()


# TypeError
# raised when two different types are combined
# print(1 + 'hello')


# IndexError
# raised when an index of a sequence does not exist
# def hello():
#     li = [1, 2, 3]
#     return li[5]
# hello()


# KeyError
# raised when a key does not exist in a dictionary
# def hello():
#     dict = {'a': 1}
#     return dict['b']
# hello()


# ZeroDivisionError
# raised when the second operator in a division is zero
# print(5 / 0)
