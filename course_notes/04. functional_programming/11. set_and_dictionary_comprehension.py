# ==== set and dictionary comprehension ====

# == set comprehension ==
# we can do the same thing we did for list. the only difference is we change the brackets to curly bracket

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(1, 10)}
my_list3 = {num**2 for num in range(1, 10)}
my_list4 = {num**2 for num in range(1, 10) if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)


# == dictionary comprehension ==
simple_dict = {
    'a': 1,
    'b': 2,
}

# action we want to do with the data, extract the key and value from variable with .items()
my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)

# adding an if statement at the end
my_dict2 = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict2)


# another example
my_dict3 = {num: num*2 for num in [1, 2, 3]}

print(my_dict3)
