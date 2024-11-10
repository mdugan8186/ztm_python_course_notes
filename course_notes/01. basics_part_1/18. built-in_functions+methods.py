# ==== built-in functions and methods ====

# built in functions seen before
# str()
# int()
# float()
# type()
# print()

# == string built-in functions ==

# len() calculates the length of the string
print(len('hellloooo')) # 9

greet  = 'hellloooo'
print(greet[0:len(greet)])


# == string methods ==

quote = 'to be or not to be'

# .upper() turns all letters into uppercase
print(quote.upper())

# .capitalize() capitalizes the first word in the string
print(quote.capitalize())

# .lower() makes every word in the string lowercase
print(quote.lower())

# .find() find the first occurrence of a letter or piece of text and returns the location
print(quote.find('be')) # 3 for position 3

# .replace() replaces all the occurrences of the first argument with the second argument
print(quote.replace('be', 'me'))

# the original quote did not change because of immutability. the methods create a new string.we didn't assign them to a variable so it will be removed from memory
print(quote)

# we are creating a new string and assigning it to a variable
quote2 = quote.replace('be', 'me')
print(quote2)
