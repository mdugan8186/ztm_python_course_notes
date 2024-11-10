# ==== immutability ====

# slicing
selfish = '01234567'
          #01234567
# selfish[start:stop:stepover]     

# strings in python are immutable, they can not be changed

# reassigning selfish will work
# selfish = 100

# reassigning the string will not work, it will produce a TypeError because strings are immutable. you can not change the value of a string once it's created
# selfish[0] = '8'
# print(selfish)

# the only way it will work is if you completely reassign the value like the examples below
selfish = selfish + '8'
# selfish = '8'
print(selfish)