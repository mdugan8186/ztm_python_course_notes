# ==== zip() ====

# zip()
# returns an iterator, from two or more iterators
# the zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc
# if the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator
# the zip() function works like a zipper. we take two iterables and zip them together
# zip(iterator1, iterator2, iterator3 ...)


my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
# [(1, 10), (2, 20), (3, 30)]

# this will take the first item from each list and zip them together in a tuple, then the second items, and so on and so on

# this will work with as many iterables as you want
their_list = [5, 4, 3]

print(list(zip(my_list, your_list, their_list)))
# [(1, 10, 5), (2, 20, 4), (3, 30, 3)]

# a real life example would be if we had a database and collected all the usernames from one part and all the phone numbers from another part of the database and zipped them together. this would work if they where all in the same order
