# augmented assignment operator

some_value = 5

# all give 7 as the answer
some_value = 5 + 2
some_value = some_value + 2

# this is the augmented assignment operator. it is shorthand instead of writing it out in the above examples
some_value += 2

# these include 
# +=
# -=
# *=
# /=

# the operator comes to the left of the equal sigh

# if this was done at the beginning you would get an error because a value was not defined
# some_value -= 5 # will throw an error


# ==== exercise ====
# Exercise Augmented Assignment Operator
# Guess what happens here before you click RUN!
counter = 0

counter += 1
# 1
counter += 1
# 2
counter += 1
# 3
counter += 1
# 4
counter -= 1
# 3
counter *= 2
# 6

print(counter) #what will this print?