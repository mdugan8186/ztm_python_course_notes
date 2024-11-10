# ==== modules in python ====

# we advanced from having our code in a single python file, next we learned about functions, and then we learned about classes. we  also learned about OOP and functional programming.

# if we have multiple python files we can link them together. we call this way of organizing code modules. each .py file is a module.

# when writing modules we use write them the same way we write variables, that is with snake case.
# we want to divide our code into chunks that make sense.
# an example would be if we worked at netflix we might a file dedicated to videos, another file dedicated to login, another file dedicated to analytics. we want to group these classes and functions together inside of a file that makes sense.

# we would want to create a utility module that is a module that is kind of like a tool belt. very simple functions that we can use all across our project


# to use the utility file in our main file we use the import command. we import, then give it the file name we want to import.
import utility
print(utility)
# <module 'utility' from '/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/8. modules_in_python/utility.py'>
# we have access to the functions with dod notation
print(utility.multiply(2, 3))

# once we make an import we will generate a pycache file. the pycache is created every time we a file with an import statement (using modules). what pycache does is when we run our program the interpreter is going to crate this pycache folder and it's going to say 'hey, i'm running this file'. it will use the C python interpreter (which is the interpreter written in C). It is actually a compiled file for the next time we run our program nothing changes because what's going to happen is instead of loading the file it's going to load up the compiles version (the pycache folder).

# we can import as many things as we want (as many files as we want)
