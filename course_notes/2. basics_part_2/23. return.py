# ==== return ====

# there are two types of functions, ones that return something (None, value, datatype) and ones that don't return anything but modifies something

# modify
def say_hi():
  print('Hi')

# returns
def add_numbers(x, y):
  return x + y


# return is saying once the code is completed return it and exit the function

# without return
def sum(num1, num2):
  num1 + num2

print(sum(4,5)) #None, because nothing was returned

# with return
def sum_2(num1, num2):
  return num1 + num2

print(sum_2(4,5))


# a function should do one thing really well 
# The return keyword is to exit a function and return a value

# this function is doing multiple things and going against the two principals of functions
def sum3(num1, num2):
  print('Hello')
  num1 + num2

sum3(5,10)


# returned values can be assigned to variables
def add_numbers2(x, y):
  return x + y

total_2 = add_numbers2(10, 5)
print(total_2)

# variables can be used as arguments
print(add_numbers2(10, total_2))

# functions can be used as arguments
print(add_numbers2(10, add_numbers2(5,10)))



# == nested functions ==

# this will return None 
def add_numbers3(x, y):
  def another_function(x, y):
    return x + y

total_3 = add_numbers3(10, 20)
print(total_3) #None

# this is one wa to use this
def add_numbers4(x, y):
  def another_function(x, y):
    return x + y
  return another_function

total_4= add_numbers4(10, 20)
print(total_4(10, 20)) #give the arguments here 

# this is another way ti use this
def add_numbers5(x, y):
  def another_function(x, y):
    return x + y
  return another_function(x, y) #another way is to add the parameters here

total_5= add_numbers5(10, 20)
print(total_5)

# the previous functions were not good and confusing. here is a cleaned up version because your function should be easy to understand
def add_num6(n1, n2):
  def another_function(num1, num2):
    return(num1 + num2)
  return(n1 + n2)

total_6 = add_num6(10, 10)
print(total_6)


# return will exit the program. anything after the return statement will not execute
def add_num7(x, y):
  return x + y
  print('I will not print')

add_num7(10, 20)