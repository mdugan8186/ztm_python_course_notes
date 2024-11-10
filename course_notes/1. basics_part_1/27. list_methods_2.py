# ==== list methods 2 ====

basket = ['a', 'b', 'c', 'd', 'e']
 

# .index() return the first index of the value. raises a ValueError if the value is not present. you can also add a starting and stopping parameter. (value, start index, stop index) this method will return a value
print(basket.index('d'))
print(basket.index('d', 0, 4))
index_of_d = basket.index('d')
print(index_of_d)


# using 'in' to see if a value is in a list. this will return a boolean
print('d' in basket)
print('f' in basket)

# this method can even be used in strings
print('e' in 'hello')
print('i' in 'hello')


# .count() returns the number of occurrences of a value. this will return a value
print(basket.count('d'))
occurrences_of_d = basket.count('d')
print(occurrences_of_d)



# == exercises ==
# Exercise List Methods
# SCROLL FOR ANSWERS!
# using this list,
basket_e = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket_e)

# 1. Remove the Banana from the list
basket_e.remove('Banana')
print(basket_e)
# 2. Remove "Blueberries" from the list.
basket_e.pop()
print(basket_e)
# 3. Put "Kiwi" at the end of the list.
basket_e.append('Kiwi')
print(basket_e)
# 4. Add "Apples" at the beginning of the list
basket_e.insert(0, 'Apples')
print(basket_e)
# 5. Count how many apples in the basket
print(basket_e.count('Apples'))
# 6. empty the basket
basket_e.clear()
print(basket_e)








# == answers ==
# 1. Remove the Banana from the list
# basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
# basket.remove('Blueberries')
# 3. Put "Kiwi" at the end of the list.
# basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
# basket.insert(0, 'Apples')
# 5. Count how many apples in the basket
# basket.count('Apples')
# 6. empty the basket
# basket.clear()
# print(basket)