# ==== dictionaries ====

# dictionary or dict is a data type and data structure. a dictionary is an unordered key value pair. keys must be hashable or immutable (strings, integers, floats, tuples). values can be any data type

dictionary = {
  'a': 1,
  'b': 2,
  'x': 3,
}

print(dictionary['b']) #2
# print(dictionary['c']) #KeyError


dictionary_2 = {
  'a': [1,2,3],
  'b': 'hello',
  'x': True,
}

print(dictionary_2['a']) #[1,2,3]
print(dictionary_2['a'][1]) #2


# list that contain dictionaries
my_list = [
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': True,
  },
  {
    'a': [4,5,6],
    'b': 'goodbye',
    'x': False,
  }
]

print(my_list)
print(my_list[0]['a'][2]) #3
print(my_list[1]['a'][2]) #6

