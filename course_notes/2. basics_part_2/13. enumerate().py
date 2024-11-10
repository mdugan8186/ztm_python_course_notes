# ==== enumerate ====

# not as common as range, but still very useful
# enumerate is useful if you need the index counter of the item  you're looping through

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# enumerate(iterable, start)

for char in enumerate('hello'):
  print(char)

# using unpacking
for i, char in enumerate('hello'):
  print(i, char)


# with a list
for i, char in enumerate([1,2,3,4]):
  print(i, char)

# with a tuple
for i, char in enumerate((4,3,2,1)):
  print(i, char)


# == exercise ==
for i, char in enumerate(list(range(100))):
  if char == 50:
    print(f'index 0f 50 is: {i}')