# ==== scope ====

# scope means what variables do i have access to?
# if the python interpreter doesn't understand or doesn't have access to it will throw a NameError

# this wil throw an error because name is not defined
# print(name) #NameError


# == global scope ==
# global scope means that anyone on the file has access to that variable
total = 100


# == function scope == 
# function scope means that the variable is only available in the function

def some_func():
  # this is only available inside the function
  another_total = 100
  # this will work because it is inside the function
  print(another_total)

# this will throw a NameError
# print(another_total)