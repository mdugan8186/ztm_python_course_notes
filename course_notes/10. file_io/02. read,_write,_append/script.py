# ==== read, write, append ====

# using this way you will have to reset the cursor and close the file at the end
# my_file = open('test.txt')

# print(my_file.read())

# my_file.close()


# the proper way to work with file i/o in python
# with - as -
# use the built in 'with' statement before you open your file. then use the 'as' keyword to name your variable. this prevents the cursor from being at the end after you read the file and having to use seek to reset the cursor. there is no need to close the file at the end of the code.

# with open('test.txt') as my_file:
#     print(my_file.read())


# == mode='' ==

# mode='r' - read - this is the default parameter for open
# with open('test.txt', mode='r') as my_file:
#     print(my_file.read())


# mode='w' - write - this is how to write in the file. it will only write the line of text in your code. anything else that was in the file will be gone
# with open('test.txt', mode='w') as my_file:
#     print(my_file.read())


# mode='r+' - read and write - this is how to read and write in a file. it will reset the cursor to 0 (the beginning of the file)
# with open('test.txt', mode='r+') as my_file:
#     print(my_file.read())


# mode='a' - append mode - when writing it puts the cursor at the end of the file instead of the begging to prevent anything already existing from being overwritten. it will allow you to keep adding text and not override anything


# write to a file
# when we write with mode='r+' the cursor resets to 0 (the begging of the file). if something already exists in the file it will be overwritten.
# to prevent this we use append mode (mode='a')
# use \n to start s new line otherwise the text will be placed on the same line
with open('test.txt', mode='a') as my_file:
    text = my_file.write('hey, it\'s me!\n')
    print(text)


# == to create a new file if one doesn't exist ==
# we can use write to create a new file
with open('sad.txt', mode='w') as another_file:
    text = another_file.write(':(')
    print(text)
