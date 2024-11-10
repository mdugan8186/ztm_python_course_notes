# ==== formatted strings ====

name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old')


# f string (f stands for format)
# to make a formatted string add an 'f' in front of the quotation mark and the names of variables in curly braces
# this is the preferred way to format a string
print(f'Hi {name}. You are {age} years old')


# .format() (the format method can also be used to format strings)
# this way will use the variables in the order they are written in the format method
print('Hi {}. You are {} years old'.format('Johnny', 55))

# using variables with .format()
print('Hi {}. You are {} years old'.format(name, age))

# another way to use variables with .format()
# computers count from 0 (zero) up, so a 0 (zero) will be the first input in the format method, 1 (one) will be the next , and so on 
print('Hi {1}. You are {0} years old'.format(name, age))

# creating your own variables with .format()
print('Hi {new_name}. You are {age} years old'.format(new_name='Sally', age=100))

# using existing variables with .format()
print('Hi {name}. You are {age} years old'.format(name=name, age=age))

# ==== exercise ====

# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))
# Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {1}.".format("Cindy", 50))
# Hello Cindy, your balance is 50.

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
# Hello Cindy, your balance is 50.

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
# Hello Cindy, your balance is 50.


# 2 How would you write this using f-string? (Scroll down for answer)

exercise_name = 'Cindy'
exercise_amount = 50
print(f'Hello {exercise_name}, your balance is {exercise_amount}')







# name = 'Cindy'
# amount = 50
# print(f"Hello {name}, your balance is {amount}.")
