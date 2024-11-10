# ==== list comprehensions ====

# comprehensions are quick ways to create lists, sets, or dictionaries in python instead of looping or appending a bunch of items to lists


# this is creating a list with a for loop and .append()
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)


# using a list comprehension
# variable = [parameter/variable for parameter/variable in iterable]

my_list2 = [char for char in 'hello']
print(my_list2)

# a way to think about this is
# 1. crate a variable (char)
# 2. then do a for loop (for char in 'hello')


# another example to populate a list of numbers
my_list3 = [num for num in range(1, 25)]

print(my_list3)


# another example (multiply the list by a certain number to get a list of sums)
# we turn the first variable into an expression
my_list4 = [num*2 for num in range(1, 10)]
print(my_list4)


# another example, have a list of numbers to the power of 2 and only keep the even numbers
# we have an expression in the begging (num**2), we loop through things (for num in range(1,10)), and an if condition at the end (if % 2 == 0)
my_list5 = [num**2 for num in range(1, 10) if num % 2 == 0]
print(my_list5)


# list comprehensions may make code shorter and possibly cleaner, but it takes away from it readability so it may be better to create a descriptive function like generate_list_of_even_numbers
