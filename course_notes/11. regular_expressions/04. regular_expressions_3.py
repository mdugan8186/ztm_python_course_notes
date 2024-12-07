# ==== regular expressions 3 ====

# a good use case for regular expressions would be collecting emails of interested customers (email validation)
# when working with regular expressions it's useful to find something online that people have used in the past (you don't have to try to reinvent the wheel), and then try to understand it
# with regular expressions you will use your google skills, you're not going to memorize the the lines for regular expressions

# step 1
# google 'python email validation regex'

# sep 2
# go to this site
# https://emailregex.com/index.html

# step 3
# copy the python code and enter it into regex (set flavor to python)
# (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

# ^ - this asserting a position at the start of the line

# [a-zA-Z0-9_.+-] - this matches a single character in a set (letters, numbers, underscore(_), dot(.), plus(+), minus(-))

# + - this is a quantifier so this matches between 1 and unlimited times

# @ - the at sign

# [a-zA-Z0-9-] - character that we can use (letters and numbers)

# + - this is a quantifier so this matches between 1 and unlimited times

# \. - this matches the character dot(.) literally

# [a-zA-Z0-9-.] - any character we want within these square brackets

# + - as long as we want

# $ - this is saying it has to end with this (this is the end of the line)


# step 3 copy the code from the code generator
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'b@b.com'
string_2 = 'Dugan'
a = pattern.search(string)
b = pattern.search(string_2)

print(a)
# <re.Match object; span=(0, 7), match='b@b.com'>

print(b)
# None
