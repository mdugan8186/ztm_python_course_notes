# ==== sets ====

# sets are unordered collections of unique objects


my_set = {1,2,3,4,5,5}
print(my_set) #{1,2,3,4,5}
# it only returns the unique sets or unique items

# .add() adds an element to the set. if the element already exists in the set it will not add it
my_set.add(100)
my_set.add(2)
print(my_set) #{1,2,3,4,5,100}
# 2 was not added because it already exists so it is not unique


# turning a list into a set
my_list = [1,2,3,4,5,5]
print(set(my_list))


# sets do not support indexing
# print(my_set[0]) #TypeError


# to check if something exists in a set
print(1 in my_set) #True


# getting the length of a set
print(len(my_set)) #6


# turning a set into a list
print(list(my_set)) #[1,2,3,4,5,100]
 

# ,copy() return a shallow copy of a set
new_set = my_set.copy()
print(new_set)


# .clear() removes all the elements from the set
my_set.clear()
print(my_set) #set()