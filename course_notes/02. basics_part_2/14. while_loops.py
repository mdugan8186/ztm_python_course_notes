# ==== while loops ====

# while condition:
#   perform task
#   stopping condition

# BE CAREFUL OF INFINITE LOOPS
# an infinite loop is created if there is no stopping condition
# i = 0
# while i < 10:
#   print(i)

# to jump out of the loop a stopping condition must be met or the break keyword must be used
i = 0
while i < 10:
  print(i)
  i += 1

# using break will only let the loop run once
j = 0
while j < 10:
  print(j)
  break


# using else blocks with a while loop
counter = 0
while counter < 10:
  print(counter)
  counter += 1
else:
  print('done with all the work')

# with a break statement
# the else block will only run if there isn't a break. this is useful if you want something to run at the end of the code only if the while loop runs. opposed to just having something after the code that isn't indented. look at counter2 and counter3 
counter2 = 0
while counter2 < 10:
  print(counter2)
  counter2 += 1
  break
else:
  print('done with all the work') #the print statement doesn't run

counter3 = 0
while counter3 < 10:
  print(counter3)
  counter3 += 1
  break
print('done with all the work') #the print statement runs
