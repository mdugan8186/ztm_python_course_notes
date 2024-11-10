# ==== tuples 2 ====

my_tuple = (1,2,3,4,5,)
print(my_tuple)

# slicing a tuple
new_tuple = my_tuple[1:2]
print(new_tuple) #(2,)
# a tuple that has a single item will tend to have a comma at the end
new_tuple_2 = my_tuple[1:4]
print(new_tuple_2) #(2,3,4)


# putting a tuple into a variable
x = my_tuple[0]
y = my_tuple[1]
print(x)
print(y)


# unpacking
d,e,f = (7,8,9)
print(d)
print(e)
print(f)

# extended iterable unpacking
a,b,c, *other = (6,7,8,9,10)
print(a)
print(b)
print(c)
print(other)


# .count() returns the number of times a specified value occurs in a tuple
print(my_tuple.count(5)) #5


# .index() searches the tuple for a specified value and returns the position of where it was found
print(my_tuple.index(5)) #4


# len() return the number of items in a container
print(len(my_tuple)) #5