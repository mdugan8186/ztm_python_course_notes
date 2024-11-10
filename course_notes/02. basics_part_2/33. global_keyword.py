# ==== global keyword ====

# parameters are local variables and considered part of the local scope
a = 10
def confusion(b):
  print(b) #local scope
  a = 90
  
confusion(300)

# this will throw an UnboundLocalError because the interpreter can con access the total from the global scope
total = 0

def count():
  total += 1
  return total

# print(count())


# == global == 
# the global keyword is used to create global variables from a no-global scope, e.g. inside a function
# to use a global variable inside a function use the global keyword

total = 0

def count2():
  global total
  total += 1
  return total

count2() #1
count2() #2
print(count2()) #3

# this is not a good way of doing things because it can become confusing when you are accessing global scope variables from inside the function scope

# == dependency injection ==
#  a better way of accessing a global variable from inside a function
# when you create a parameter we pass in the variable. then we pass that variable as an argument too

total = 0

def count3(total):
  total += 1
  return total

print(count3(count3(count3(total)))) #3





