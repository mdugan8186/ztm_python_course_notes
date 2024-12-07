# ==== regular expressions 2 ====

import re

# simple text patterns
pattern = re.compile('search this inside of this text please!')

string = 'search this inside of this text please! Dugan'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

# print(d)


# where regular expressions become really useful is for advanced patterns
# you can think of regular expressions as entire language in itself, with different patterns that you use to find patterns inside of texts
# the whole world of regular expressions is really complicated


# regex101.com can be used for regular expressions. it has many tools that can be used
# in flavors select python
# you can use the common tokens to select what you want
# if you go to tools and select code generator it will give you a sample code in python

# an example would be this
# the r stands for a raw string
# the r says this is a raw string, ignore everything that python interpreter might interpret, i want this to just be a pure string
# regex = r"([a-zA-Z]).([a])"

pattern_2 = re.compile(r"([a-zA-Z]).([a])")

string_2 = 'search this inside of this text please! Dugan'

e = pattern_2.search(string_2)

print(e.group())  # sea
print(e.group(1))  # s
print(e.group(2))  # a


# another useful thing is that you can search in the quick reference
