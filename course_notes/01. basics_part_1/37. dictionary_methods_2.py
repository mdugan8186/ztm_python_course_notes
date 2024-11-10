# ==== dictionary methods 2 ====

user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20,
}


# using 'in' to look for an item
print('basket' in user) #True
print('size' in user) #False


# .keys() returns a list containing the dictionary's keys
print('age' in user.keys())
print(user.keys())


# .values() returns a list of all the values in the dictionary
print('hello' in user.values())
print(user.values())


# .items() returns a list containing a tuple for each key value pair
print(user.items())


# .copy() returns a copy of the dictionary
user_2 = user.copy()
print(user_2)


# .update() updates the dictionary with the specified key-value pairs
print(user.update({'age': 55}))
print(user)

# if the key doesn't exist a new key:value will be created
print(user.update({'ages': 55}))
print(user)


# .pop() removes the specified key and returns the corresponding value. if the key is not found, it returns the default if given; otherwise it raises a KeyError.
print(user.pop('age')) #55
print(user) #age was removed


# ,popitem() removes the last inserted key-value pair
print(user.popitem()) #('ages', '55')
print(user)


# .clear() removes all the elements from the dictionary
print(user.clear()) #None

# or 

user.clear()
print(user) #{}



# == exercise ==

# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 by copying the previous user and update the age value and username value.


user_exercise = {
  'age': 42,
  'user_name': 'mdugan8186',
  'weapons': None,
  'is_active': True,
  'clan': None
}

print(user_exercise)
print(user_exercise.keys())

user_exercise['weapons'] = 'axe'
print(user_exercise['weapons'])

user_exercise['is_banned'] = False
print(user_exercise['is_banned'])

user_exercise['is_banned'] = True
print(user_exercise['is_banned'])

user_exercise_2 = user_exercise.copy()
user_exercise_2.update({'age': 22, 'user_name': 'aliensRule420'})
print(user_exercise_2)





#ANSWERS BELOW:

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
# user_profile = {
#     'age': 0,
#     'username': ' ',
#     'weapons': None,
#     'is_active': False,
#     'clan': None
# }

# 2 iterate and print all the keys in the above user.
# print(user_profile.keys())

# 3 Add a new weapon to your user
# user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
# user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
# user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
# user2 = user_profile.copy()
# user2.update({'age': 50, 'username': 'User2'})
# print(user_profile)
# print(user2)