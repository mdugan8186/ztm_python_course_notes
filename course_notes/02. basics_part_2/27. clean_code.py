# ==== clean code ====

# original code
def is_even(num):
  if num % 2 == 0:
    return True
  elif num % 2 != 0:
    return False
  
print(is_even(50))


# cleaned up code
# step 1
# the elif is not needed, an else is good because if not True it is false
def is_even2(num):
  if num % 2 == 0:
    return True
  else:
    return False
  
print(is_even2(50))
  
# step 2 the else is not needed because if if it is not true the if code block will not run
def is_even3(num):
  if num % 2 == 0:
    return True
  return False

print(is_even3(50))

# step 3 since you're returning True or False directly you can use an expression that evaluates to a boolean 
def is_even4(num):
  return num % 2 == 0

print(is_even4(50))





