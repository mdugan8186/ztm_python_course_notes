# ==== logical operators ====

# and 
# or
# > 'greater than'
# < 'less than'
# == 'equal to' it must be 2 equal signs. a single equal is a key word used to assign variables
# >= 'greater than' or 'equal to'
# <= 'less than' or 'equal to'
# != 'not equal to'
# not 'the opposite', it can be used with or without parentheses


print(4 > 5) #False
print(4 < 5) #True
print(4 == 5) #False
print('hello' == 'hello') #True
print(1 < 2 < 3 < 4) #True
print(1 < 2 > 3 < 4) #False
print(1 >= 0) #True
print(1 <= 0) #False
print(0 != 0) #False
print(0 != 1) #True
print(not(True)) #False
print(not False) #True
print(not 1 == 1) #False

# you would not see the example below in real code
# when comparing characters using the < or > python converts it to an integer according to ASCII Table
print('a' > 'b') #False
print('a' > 'A') #True
# a is 97 decimal
# b is 98 decimal
# A is 65 decimal
# B is 66 decimal