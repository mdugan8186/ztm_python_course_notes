# ==== tuple ====

# tuples are another data type and data structure
# tuples are like lists but unlike list they can not be modified, they are immutable. think of them as immutable lists 
# a benefit of a tuple is that it will signal to other developers that you have  a list that you don't want to change. since they are less flexible they are more performant than lists
# a disadvantage is that it is less flexible than a list. you can't sort, reverse, or any other way to modify it 
# if you don't need a list to change use a tuple. a good use of a tuple would be geographic location and coordinates

my_tuple = (1,2,3,4,5)

# if you try to modify a tuple you will get an error
# my_tuple[1] = 'z' #TypeError

# accessing an element
print(my_tuple[1]) #2

# finding an element
print(5 in my_tuple) #True 



# tuples ca be a valid key for a dictionary
user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20,
  (1,2): [4,5,6]
}
print(user.items())
# the dictionary method .items() returns an array of tuples

# accessing a tuple in a dictionary
print(user[(1,2)]) #[4,5,6]

