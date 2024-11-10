# ==== docstrings ====

# docstrings are a way to comment inside of our function in a way that if another person is using the function they can see what it does in the code editor, similar to a tool tip in a webpage
# they are created by using three quotation marks (''') before and after the info you're going to enter


def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)

test('!!!!')

# to see the docstring call the function as normal. then hover over it with your cursor and a popup window will show what the function is and what you wrote in the docstring. it is the same as viewing the info of a built in function like len()
test('test')

# help() Executes the built-in help system
# using help() is another way of viewing the docstring. you do not want to call the function you are trying to vies so do not use parenthesis 
# help(test)
# to exit the help screen just type in 'q' (press the q key)

# dunder method 
# dunder methods use double underscores (__ method__)
# using a dunder method called (doc)  is another way of viewing the docstring (this will be explained later in the course)

print(test.__doc__)

