# ==== for loops ====

# loops allow us to run lines of code over snd over
# for loops allow us to iterate over anything that has a collection of items


# for(keyword) item(variable that can be any name) in(keyword) iterable(something that that ks able to get looped over):
#   indentation for code block

# strings
for item in 'hello':
  print(item)

# lists
for item in [1,2,3,4]:
  print(item)

# sets
for item in {1,2,3,4}:
  print(item)

# tuple
for item in (1,2,3,4):
  print(item)


# outside of the indentation (code block) the loop will stop and go onto the next task
for item in ['one', 'two', 'three']:
  print(item)
  print(item)
  print(item)
print(item) #this will actually print the last item in the loop
print('i\'m out of the loop')


# nested loops
for item in [1,2,3,4]:
  for x in ['a', 'b', 'c']:
    print(item, x)



