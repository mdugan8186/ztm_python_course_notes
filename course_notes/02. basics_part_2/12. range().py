# ==== range() ====

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# range(start, stop, step)
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

print(range(10)) #prints a range object range(0, 10)


# most cases of range will be in a for loop
for num in range(0, 10):
  print(num)

for num in range(0, 3):
  print('email list')

# if the variable is not needed in the for loop an underscore (_) can be used 
for _ in range(0, 3):
  print(_)

for _ in range(0, 3):
  print('no variable needed')


# using the third parameter
for _ in range(0, 10, 2):
  print(_)


# counting backwards/ reverse
for _ in range(5, 0, -1):
  print(_)

for _ in range(10, 0, -2):
  print(_)


# quick way to create a list that has integers
for _ in range(2):
  print(list(range(10)))