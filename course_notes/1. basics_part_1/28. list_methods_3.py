# ==== list methods 3 ====

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']


# .sort() sorts the list in ascending order and return None. this modifies the list in place
print(basket.sort()) # None
basket.sort()
print(basket)


# built in function
# sorted() return a new list containing all items from the iterable in ascending order
basket_2 = [3,10,6,4,9,2,1]

# new list
print(sorted(basket_2))
# original list is unchanged
print(basket_2)

# reverse sorted, use by adding the reverse parameter. False is ascending, True is descending
print(sorted(basket_2, reverse=True))


# .copy() this return a copy of the list
basket_3 = basket.copy()
basket.pop()
print(basket)
print(basket_3)

# .copy() can take place of using the [:] to copy a list
basket_3 = basket[:]
basket.pop()
print(basket)
print(basket_3)


# .reverse() reveres the list. this method does not return anything
basket.reverse()
print(basket)



# to get a sorted and reversed list first use .sort(), then use .reverse
basket_4 = [9,3,6,4,7,1]
basket_4.sort()
basket_4.reverse()
print(basket_4)
