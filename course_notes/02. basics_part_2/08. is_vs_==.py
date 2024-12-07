# ==== (is vs ==) ====

# == quick quiz ==
print(True == 1) #True
print('' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True
print('end of first part')

# double equal (==) checks for equality or equality of value

# python would convert these to the same type on its own but would look like this
print(True  == bool(1)) #True
#     True == True

print('' == str(1)) #False
#     False == True

print([] == 1) #False
#     False == True

print(10 == int(10.0)) #True
#     10   10

print([] == []) #True
#     False == False

print('end of second part')
# you should be checking two of the same types so you won't see the above example in real code


# == is ==
# is actually checks if the location in memory where this value is stored is the same  

# for these to be true they actually have to be the same ex. True is True
print(True is 1) #False
print(True is True) #True

print('' is 1) #False
print('' is '') #True

print([] is 1) #False
print([] is []) #False
# this is tricky (and advanced) because every time a list is created it's added in memory somewhere, so both lists are stored in different locations in memory (they are two completely different lists)

print(10 is 10.0) #False
print(10 is 10) #True

print([] is []) #False

# this works with numbers and strings because underneath the hood these are types that are very simple that are in memory but are in one location
# since lists are a data structure every time we create one it's created in a new location (this also includes dictionaries, tuples, and sets)

# another example 
print('another example below')
a = [1,2,3]
b = [1,2,3]
print(a is b) #False
print(a is a) #True

print(a == b) #True
# it will work with the double equality sign because it checks only the values
