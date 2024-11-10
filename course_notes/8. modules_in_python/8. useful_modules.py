# ==== useful modules ====

# collections
from collections import Counter, defaultdict, OrderedDict

# Counter - creates a dictionary that keeps track how many times an item occurred in an iterable
li = [1, 2, 3, 4, 5, 6, 7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))


# defaultdict - if something doesn't exist it will give you a default value that we enter as a parameter. the parameter is a function that we;re not going to use, such as int or lambda: 5 or lambda: 'does not exist'
dictionary = {'a': 1, 'b': 2}
print(dictionary['a'])
# print(dictionary['c'])  # this will throw a KeyError

dictionary2 = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary2['c'])


# OrderedDict - an ordered dictionary retains the order that you insert into a dictionary
# == note at bottom ==
dict = OrderedDict()
dict['a'] = 1
dict['b'] = 2

dict2 = OrderedDict()
dict2['b'] = 2
dict2['a'] = 1

print(dict)
print(dict2)

print(dict2 == dict)
# this will print False because the order of the dictionary matters with OrderedDict


# This will print True because the order does not matter with a regular dictionary
dict3 = {'a': 1, 'b': 2, 'c': 100}
dict4 = {'c': 100, 'a': 1, 'b': 2}

print(dict3)
print(dict4)
print(dict3 == dict4)


# == note ==
# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
