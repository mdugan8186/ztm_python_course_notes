# ==== dictionary keys ====

# keys must be hashable or immutable (strings, integers, floats, tuples) which means they can not change
# the majority of the time the key is a string and something descriptive


dictionary = {
  123: [1,2,3],
  True: 'hello',
  # [100]: True, #can not use a list as a key
}

print(dictionary[123]) #[1,2,3]
print(dictionary[True]) #hello
# print(dictionary[[100]]) #TypeError


# if the same key is used again Python will use the last key and overwrite the first key
dictionary_2 = {
  '123': [1,2,3],
  '123': 'hello'
}

print(dictionary_2['123'])