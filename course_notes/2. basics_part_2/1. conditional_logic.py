# ==== conditional logic ====

# if 'condition': this will evaluate to True or False, if the conditional is true the code block will run 
#   code must be indented to be part of the if statement
# elif 'condition': this will evaluate to true or false and run if true. there can be as many elif statements as needed
# else: this will run if all other conditions are false


is_old = True
is_licensed = True

if is_old:
  print('You are old enough to drive')
elif is_licensed:
  print('you can drive now')
else:
  print('You are not of age')

print('check check')
# python will not see the print statement as part of the if statement


# == using other key words as part of the conditions ==  

# 'and' both expressions must be True for it to run 
if is_old and is_licensed:
  print('You are old enough to drive')
else:
  print('You are not of age')


