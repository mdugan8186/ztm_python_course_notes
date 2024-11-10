# ==== list methods ====

# == built in functions ==
# len() calculates the length of a list
basket = [1,2,3,4,5]
print(len(basket))


# == adding list methods ==

# .append() adds an item at the end of the list
new_list = basket.append(100)
print(new_list) # will print 'none' because append can only modify the original list, it changes the list in place. it does not create a new list or produce a value (return anything)
print(basket) # the original list is modified 
# to get new_list to equal basket it must be assigned to it in a variable
new_list = basket
print(new_list)
# after we append, we can then assign


# .insert() takes in two parameters (index, object to be inserted). it inserts an object before the index. this method only modifies the list, it does not create a new list or return anything
basket.insert(4, 4.5)
print(basket)


# .extend() takes an iterable (something you can iterate or loop over). extends the list by appending elements from the iterable. this method only modifies the list, it does not create a new list or return anything
basket.extend([101, 102])
print(basket)


# == removing list methods ==

# .pop() removes and returns item at index (default last).raises IndexError if the list is empty or index is out of range. this method will return a value
basket.pop()
print(basket)
# return a value
popped_basket = basket.pop(4) #removes at the index
print(popped_basket)
print(basket)


# .remove() removes th first occurrence of a value. raises a ValueError if the value is not present. this method only modifies the list, it does not create a new list or return anything
basket.remove(101)
print(basket)


# .clear() removes all the elements from the list. this method only modifies the list, it does not create a new list or return anything
basket.clear()
print(basket)