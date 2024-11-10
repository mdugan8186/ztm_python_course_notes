# ==== functions ====

# functions are useful for tasks that you want to repeat. avoiding repeating yourself and using the DRY principal

# to make a function use the keyword def(define) followed by the functions name then a set of parenthesis with any parameters inside it and then use a colon to close it. the code block must be indented

# def function name(parameters):
  # indentation and code block

def say_hello():
  print('hello')

# to use a function you must call it
# to call use the function name with parenthesis and any arguments inside of them. you must use parenthesis after the function name or it will not run

# function name(arguments)

say_hello()



# for example code below
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# instead of running code multiple times like this
for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end="")
    else:
      print(' ', end="")
  print('')
for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end="")
    else:
      print(' ', end="")
  print()



# by using a function you don't have to write the same code multiple times
def make_tree():
  for row in picture:
    for pixel in row:
      if pixel == 1:
        print('*', end="")
      else:
        print(' ', end="")
    print('')

make_tree()
# if you try to call the function before it is defined you will gat a NameError


print(make_tree()) #None

# without the parenthesis it will say the is a function followed by its name and location in memory
print(make_tree) #<function make_tree at 0x770d9a81ccc0>