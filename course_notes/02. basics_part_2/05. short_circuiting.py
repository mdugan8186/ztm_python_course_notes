# ==== short circuiting ====

is_friend = True
is_user = True

print(is_friend and is_user)

if is_friend and is_user:
  print('best friends forever')


# == or ==
# or says if either one of the conditions is true run the code block, or is more performant
if is_friend or is_user:
  print('best friends forever')


# In Python, short-circuiting refers to the evaluation behavior of logical operators ('and' and 'or'). This mechanism allows the interpreter to skip evaluating the second operand if the result can be determined from the first operand alone.
