# ==== dictionary methods ====

user = {
  'basket': [1,2,3],
  'greet': 'hello',
}

print(user['basket'])


# if a key does not exist you will get an error
# print(user['age']) #KeyError

# .get() returns the value for the key if the key is in the dictionary, else it returns the default (which is None) unless a default was made.
print(user.get('age')) #None

# adding a default to .get()
print(user.get('age', 55)) #55


# == another way create a dictionary ==
# this is not very common
# dict(key=value)
user_2 = dict(name='JohnJohn')
print(user_2)


