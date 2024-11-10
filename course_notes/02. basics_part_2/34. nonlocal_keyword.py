# ==== nonlocal keyword ====

# nonlocal
# the nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# use the keyword nonlocal to declare that the variable is not local.
# it is using the parent variable while inside the local variable
# this will not work with global variables

def outer():
  x = 'local'
  def inner():
    nonlocal x # this means we will use the variable from the parent function
    x = 'nonlocal'
    print('inner:', x)

  inner()
  print('outer:', x)

outer()