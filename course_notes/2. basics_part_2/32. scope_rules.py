# ==== scope rules ==== 

# guess the outcome

a = 1

def confusion():
  a = 5
  return a

print(a) #1
print(confusion()) #5

print(confusion()) #5
print(a) #1

# a gets taken from the global scope and confusion gets taken from the confusion function. even if the are switched oit will still give the same answer


# the rules the python interpreter uses to check a variable
# 1. start with local scope
# 2. check to see if there is a parent to the local scope
# 3. if there is nothing in the local or parent scope it will check the global scope
# 4. if the variable is not in the global scope the interpreter will check built in python functions (pythons predefined functions)

def parent():
  a = 10
  def confusion2():
    return a
  return confusion2()

print(parent()) #10
print(a) #1

# since a is not in confusion2 the interpreter will look to the parent of confusion2 which is parent and use the a variable from there

a= 1

def parent2():
  def confusion3():
    return a
  return confusion3()

print(parent2()) #1
print(a) #1

# since a in not in the local scope or the parents local scope the interpreter moves on to check the global scope for a

a= 1

def parent3():
  def confusion4():
    return sum
  return confusion4()

print(parent3()) #<built-in function sum>
print(a) #1