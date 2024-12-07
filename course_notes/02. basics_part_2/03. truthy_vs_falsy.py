# ==== truthy vs falsy ====

# == these are using booleans ==

# python will convert the conditions to booleans automatically
is_old = 'hello'
is_licensed = 5

# strings, integers, floats, and True are truthy
# 0, '', [], {}, () (empty sequences and collections), None, and False are falsy

# it is basically saying 
# bool(is_old)  
# bool(is_licensed)
if is_old and is_licensed:
  print('You are old enough to drive')
else:
  print('You are not of age')


# == these are truthy ==

# this is just an example to check if this person has a username and password
password = '123'
username = 'johnny'

if password and username:
  print('has a password and username')
else:
  print('not a member')




