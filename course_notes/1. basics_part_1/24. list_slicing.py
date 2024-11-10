# ==== list slicing ====

# == list slicing ==
# this is similar to string slicing
str = 'hellloooo'
str[0:2:1]
# [start:stop:stepover]


amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys',
  'grapes'
]

print(amazon_cart)
print(amazon_cart[0:2])
# notebooks sunglasses
print(amazon_cart[0::2])
# entire cart but skip every second item
# notebooks toys


# lists are mutable
amazon_cart[0] = ['laptop']
print(amazon_cart)

print(amazon_cart[1:3])
# sunglasses toys

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)


# because of how python memory works if you want to create a list with an already existing list you need to use list slicing 

stuff_cart = [
  'stuff',
  'more stuff',
  'other stuff',
  'not my stuff'
]

# if you create a new list by copying another list and you don't use slicing the new list will equal the old list. this means that if anything in the new list is changed it will also mutate the original list
 
# this will cause the old list to be mutated if the new list is changed
# new_stuff_cart = stuff_cart

# you must slicing to create a new list from another list
new_stuff_cart = stuff_cart[:]



# == exercise ==

#What is the output of this code?
#Before you click RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
# b
print(new_list[-2])
# b
print(new_list[1:3])
# b c
new_list[0] = 'z'

print(new_list)
# z b c
my_list = [1,2,3]

bonus = my_list + [5]

my_list[0] = 'z'

print(my_list)
# z 2 3 
print(bonus)
# 1 2 3 5