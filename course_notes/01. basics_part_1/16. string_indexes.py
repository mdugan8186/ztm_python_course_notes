# ==== string indexes ====

# str (or strings are an ordered sequence of characters)

# when a string is stored in memory it would be stored in these locations. each location would corresponds with a value
# 'me me me'
#  01234567

# using bracket notation to access a character with it's index
# you can access different parts of a string using its index
selfish = 'me me me'
         # 01234567

print(selfish[0]) # m
print(selfish[7]) # e
print(selfish)

# slice or slicing []
# slicing strings to create (access) substrings with bracket notation
# using bracket notation to access a substring with slice
numbers = '01234567'
# [start:stop:stepover]
# start is the index it will start at
# stop is the index it will stop at, but it doesn't include that index
# stepover is how many indices it will skip or step over. the default is 1

print(numbers[0:2]) # 01
print(numbers[0:7]) # 0123456
print(numbers[0:8]) # 01234567

print(numbers[0:8:2]) # 0246

# [1:]
# this will start at the given index and then go all the way to the end 
print(numbers[2:]) # 234567

# [:5]
# this will start at the begging and stop at the given index
print(numbers[:5]) # 01234

# [::1]
# this will be the default behavior (starting at 0, ends when the string ends, and stepover once)
print(numbers[::1]) # 01234567

# [-1]
# negative indices
print(numbers[-1]) # 7
print(numbers[-2]) # 6
print(numbers[-3]) # 5

# [::-1]
# this will reverse the string or order
# it is saying start, stop, but stepover from the back
print(numbers[::-1]) # 76543210
print(numbers[::-2]) # 7531


# ==== exercise ====

#Guess the output of each print statement before you click RUN!
python = 'I am PYTHON'

print(python[1:4])
# am
print(python[1:])
# am PYTHON
print(python[:])
# I am PYTHON
print(python[1:100])
# (nothing)
print(python[-1])
# N
print(python[-4])
# T
print(python[:-3])
# I am PYT
print(python[-3:])
# HON
print(python[::-1])
# NOHTYP ma I