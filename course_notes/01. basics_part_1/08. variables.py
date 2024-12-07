# ==== Variables ====

# the best practice for writing variables in python
# snake_case
# start with lowercase or underscore
# case sensitive (snake_case and snakE_case are different variables)
# don't overwrite keywords  
# make variables as descriptive as possible

user_iq = 190
user_iq2 = 190

_user_iq = 190
# underscore signifies a private variable

print(user_iq)
print(user_iq2)
print(_user_iq)

# case sensitive
user_IQ = 190
# can't be accessed with 
# print(user_iq)

# keyword
# print = 190
# print(print) # throws an error

# variables can be reassigned
iq = 190
user_age = iq / 4
a = user_age

print(iq)
print(user_age)
print(a)

# constants (are things that never change or are not meant to be changed in a program)
# constants are in all capitals
PI = 3.14


# dunder (stands for double underscore) (meant to be left alone, should not be touched)
# do not make variables with double underscores
__hihi = 'hi'


# == quick trick ==
# quick way to assign muliple variables
b,c,d = 1,2,3

print(b)
print(c)
print(d)

