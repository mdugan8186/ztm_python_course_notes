# ==== regular expressions ====

# regular expressions are not unique to python, they are all over programming languages

# regular expressions are useful for checking validation emails, passwords requirements, or check if a piece of string exists in a piece of text

# python comes with a regular expression module
import re

string = 'search inside of this text please!'

# this is a simple way for us to search something inside a string
print('search' in string)  # True


# regular expressions are a little more powerful than the code above

# search(pattern, string, flags)
print(re.search('this', string))
# <re.Match object; span=(17, 21), match='this'>
# the output of a regular expression is a Match object, it also gives the span (or where if occurs in the string)


a = re.search('this', string)

# span() - tells us where the string occurs as a tuple
print(a. span())  # (17, 21)

# start() - when the text starts
print(a.start())  # 17

# end() - where the text ends
print(a.end())  # 21

# group - returns the part of the string where there was the match
# group is useful when we're trying to do multiple searches
print(a.group())  # this


# if we search for something that doesn't exist it will return None causing an AttributeError to bge thrown


# we can make this more advanced by checking for a pattern
# we can create a pattern with re.compile and entering what we want to look for
pattern = re.compile('this')
string_2 = 'search this inside of this text please!'

# instead of using re.search we use pattern.search. this also eliminates entering the pattern you are looking for
b = pattern.search(string_2)
print(b.group())

# findall() - finds all the instances of the match
c = pattern.findall(string_2)
print(c)

# fullmatch() - this makes sure everything matches fully. the entire string must match, not just pieces out of it
pattern_2 = re.compile('search this inside of this text please!')

d = pattern.fullmatch(string_2)
print(d)
# this returns None because the entire string does not match

e = pattern_2.fullmatch(string_2)
print(e)
# this returns a match object because everything in the string matches

# match() - this matches the string then doesn't care what comes after it
string_3 = ('search this inside of this text please! stuff and more stuff')
f = pattern_2.match(string_3)
print(f)
