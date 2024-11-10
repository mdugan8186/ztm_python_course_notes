# ==== break, continue, pass ====

my_list = [1,2,3]


# == break == 
# The break keyword is used to break out a for loop, or a while loop.

for item in my_list:
  print(item)
  break

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  break


# == continue ==
# The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration (or back to the beginning of the loop)

# these will print 
for item in my_list:
  print(item)
  continue

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  continue

# these will not print because continue states to go back to the beginning of the loop
for item in my_list:
  continue
  print(item)

i = 0
while i < len(my_list):
  i += 1
  continue
  print(my_list[i])


# pass
# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

for item in my_list:
  # thinking about it
  pass #this prevents an error if the code block is empty

