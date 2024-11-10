# ==== filter() ====

# filter()
# use a filter function to exclude items in an iterable object
# the filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not
# filter() checks the items by using True of False
# filter(function, iterable)


# when adding the function to filter() we don't want to invoke it


my_list = [1, 2, 3, 4, 5, 6, 7]


# this function returns True or False
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))


# a real world example would be filtering out a list of users starting with the letter 'A'

user_list = ['Red Queen', 'Alice', 'Mad Hatter', 'Adam']


def filter_a_names(item):
    if 'A' in item:
        return True


a_user_names = list(filter(filter_a_names, user_list))

print(a_user_names)
