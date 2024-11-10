# ==== __name__ ====

import utility
from utility import multiply, divide
from shopping.more_shopping import shopping_cart

# we would wrap our entire code in the __name__ code
if __name__ == '__main__':

    print(shopping_cart.buy('apple'))
    print(divide(5, 2))
    print(multiply(5, 2))


# in order to finalize our understanding of modules we need to go over the concept of __main__
# you will see a lot of code like this working with python
# if __name__ == '__main__':


# by putting print(__name__) at the tops of the utility and shopping modules we will get their name. utility and shopping.more_shopping.shopping_cart when we run the main file. this happens because the interpreter goes line by line and during the import line it goes to that file and runs that file and by doing this puts that file in memory


# running this code will always give you __main__ in the output because it is the main file regardless of its name
print(__name__)

# this code will be run to make sure that the file we are running is the __main__ file or module because that one single file imports different modules and runs them
# if __name__ == '__main__':
# print('please run this')

# this code will not run if it was in another file or module because they are not __main__

# if you put it in another file or module it will throw an ImportError


# we will also see the __main__ in classes
class Student():
    pass


st1 = Student()
print(type(st1))
# <class '__main__.Student'>

# the above code is simply saying that the class Student was created in the __main__ file.

# if it was created in the utility file it would say this
print(type(utility.st2))
# <class 'utility.Student2'>
