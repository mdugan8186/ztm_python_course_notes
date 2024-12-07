# ==== map() ====

# map()
# returns the specified iterator with the specified function applied to each item
# the map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter
# map(function, iterables)
# map(action we want to take, [1,2,3])

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

# this will give us the memory location
print(map(multiply_by2, [1, 2, 3]))
# <map object at 0x79da5d5ffe20>

# in order to see this we must put it into a list, nut this WILL throw an error due to the function itself
# print(list(map(multiply_by2, [1, 2, 3])))


# to get map() to work properly we must edit our function. with map() we would no longer need to do the creation of a list, then appending to the new list. we just need to give map() some data and the data gets acted upon by the function. all we need to do for the map function is to have a function that returns what you want done

def multiply_by3(item):
    return item * 3


# we just have to enter the function, we aren't invoking it. map() will call it for us. then it will iterate over the data performing the action we entered
print(list(map(multiply_by3, [1, 2, 3])))

# map() wil not modify data outside of it's scope because it is a pure function
my_list = [1, 2, 3]
print(list(map(multiply_by3, my_list)))
print(my_list)


# a real life example of using map() would be is we had to change all usernames to uppercase

username_list = ['rick', 'morty', 'summer', 'beth', 'jerry']


def change_to_uppercase(item):
    return item.upper()


fixed_usernames = list(map(change_to_uppercase, username_list))

print(fixed_usernames)
