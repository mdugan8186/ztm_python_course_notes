# ==== *args and **kwargs ====

# *args (arguments) 
# **kwargs (keyword arguments)
# args and kwargs are variables that we are creating that can be named anything. the standard is to name then args and kwargs 

# sum() return the sum of a 'start' value (default: 0) plus an iterable of numbers

# this will give you a TypeError because there are more arguments then parameters
# def super_func(args):
#   return sum(args)

# super_func(1,2,3,4,5)

# this can be fixed with *args. with *args we are saying this can accept any number of positional arguments
def super_func(*args):
  print(args) #(tuple) (1,2,4,5)
  print(*args) #1 2 3 4 5
  return sum(args)

print(super_func(1,2,3,4,5))

# **kwargs allow us to add any number of keywords arguments
def super_func2(*args, **kwargs):
  print(kwargs) #(dictionary) {'num1': 5, 'num2': 10}
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func2(1,2,3,4,5, num1=5, num2=10))

# == rule of order ==
# parameters, *args, default parameters, **kwargs

# this is just an example to show the order. you would alost never have all of these, usually you're only using one or two of these. and you'd never write a function like this because it is super confusing
def super_func3(name, *args, i='hi', **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func3('Andy', 1,2,3,4,5, num1=5, num2=10))


