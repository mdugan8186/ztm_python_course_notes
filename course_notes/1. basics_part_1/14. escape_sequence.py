# ==== escape sequence ====

# weather = 'Is's sunny'
# this will create an error because python thinks there is a string and another string starting

# to fix it you can use double quotes
weather = "It's sunny"

# by putting something in quotation marks will create another problem/ error
# weather = "It's "kind of" sunny"

# an escape sequence is using a backwards slash in front of the quotation mark you want ignored so python won't think it's the end of the string. you're letting python know whatever comes after the backwards slash is a string
weather = 'It\'s sunny'
print(weather)

weather = "It's \"kind of\" sunny"
print(weather)

weather = "It\\s \"kind of\" sunny"
print(weather)

# /t will create a tab
weather = "\t It's \"kind of\" sunny"
print(weather)

# \n will create a new line
weather = "It's \"kind of\" sunny \nhope you have a good day!"
print(weather)

