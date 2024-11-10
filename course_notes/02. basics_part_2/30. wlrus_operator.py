# ==== walrus operator ====

# as of version 3.8 there is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus

# you might not see it often. it's essentially a  way for us to minimize  doing calculations that are similar inside of if statements or while statement where we want to  do something based on a condition and then calculate that value again


a = 'hellloooooo'

# in this code we are repeating ourselves with the len(a)
if len(a) > 10:
  print(f'too long, {len(a)} elements')

# we can use the walrus operator to prevent this
# first we wrap what we want to duplicate in parenthesis, then create a variable (n), followed by the walrus operator, and finally that what we are going to duplicate or repeat
# this assigns a new variable to values as part of a larger expression
if (n := len(a)) > 10:
  print(f'too long, {n} elements')


# another example
while (n := len(a)) > 1:
  print(n)
  a = a[:-1]

print(a)
