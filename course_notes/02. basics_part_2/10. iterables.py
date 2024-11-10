# ==== iterables ====

# iterable means it is an object or a collection that can be iterated (or looped) over 
# iterables(noun) - can be lists, dictionary, tuple, set, string
# iterated(verb) - means we can go one by one to check each item in the collection


# dictionary
user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False,
} 

# this prints the keys of the dictionary
for item in user:
  print(item)

# dictionary methods for looping over keys, values, and key value pairs

# .items() returns a list containing a tuple for each key value pair
for item in user.items():
  print(item)

# .values() returns a list of all the values in the dictionary
for item in user.values():
  print(item)

# .keys() returns a list containing the dictionary's keys
for item in user.keys():
  print(item)

# using tuple unpacking to get the key and value
for item in user.items():
  key, value = item
  print(key, value)

# shorter way of tuple unpacking
# short hand would use k and v, but can be any variables that would help your code be more readable
for key, value in user.items():
  print(key, value)


# this will create an TypeError because 50 in not an object that can be iterated over
# for item in 50:
  # print(item)