# ==== generators ====

# generators are available in python and allow us to generate sequential values over time

# an example of a generator is range(10). a generator is a special type of thing in python that allows us to a special keyword called yield and it ca pause and resume functions.


# example
# range will create a number one by one
range(10)

# what a list does is actually creates a list of items in memory
list(range(10))


# when we make a list like we did in the example above we are essentially doing what this function is doing. we're using range to create a list and return the result which will live in memory
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)
print(my_list)
# when this list is printed it will live in memory. so this is taking up space right now

# now range is a generator. and a generator is a little bit different because it's output is not being held up in memory.
#  when we do the for loop in the above function range doesn't create a list on its own and then start iterating. it's going to say hey as a range i'm going to give you first a number zero, then i'm going to give you the number one, and so on and so on until the end of the number inputted as the argument. so in memory it never creates this list like we have with my_list


# another way to look at it is if we printed a list with a range of 100 print(list(range(100))) we wouldn't be able to use the list until it finished generating, and only then could we use it and then it's going to access that list in memory and then we're able to use it.
# a more efficient way is to use a generator and actually generate these one at a time without taking up space in memory
