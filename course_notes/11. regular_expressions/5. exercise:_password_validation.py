# ==== exercise: password validation ====

# write a password validator
# use regex to write a regular expression
# at least 8 characters long
# can contain any sort of letters, numbers, and these symbols $%#@


# == my code ==

import re

pattern = re.compile(r"^[a-zA-Z0-9$%#@]{8,}$")

string = 'ab56%$dc'
string2 = 'cd12@#a'
string3 = 'ab23@#w1$%'
string4 = 'fg78&$as'

a = pattern.search(string)
b = pattern.search(string2)
c = pattern.search(string3)
d = pattern.search(string4)


print(a)
print(b)
print(c)
print(d)


# his code
# he added must end with a number

pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

password = 'nk4r5fw23%$9'

check = pattern2.fullmatch(password)

print(check)
