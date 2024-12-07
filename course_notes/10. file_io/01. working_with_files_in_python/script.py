# ==== working with files in python ====

# FILE I/O
# i/o stands for input / output
# most of the times machines are not communicating in just one environment. an example would be having your code in an ide or an editor and you want to speak to another website, something thats on your desktop, two different machines are communicating with each other, a database
# i/o simply means i want you to input something from the outside world and output something into the outside world
# reading files is one of the most common ways we use i/o

# an example would be to write a script that compresses images
# input image
# output compressed image

# adding a watermark to all your pdf pages
# input pdf
# output new version of the pdf


# python has a built in function that allows us to open and write to files
# make sure you are in the right directory (check with pwd and ls in the terminal)

# == open ==
# use open and put the file name in the parenthesis
my_file = open('test.txt')
print(my_file)
# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>


# .read() - allows you to read the file
print(my_file.read())

# you can only read the file once because after it is read the cursor is at the end of the file and there is nothing to be read there
# to get around this we cn use seek()


# seek() - moves our cursor to whatever index we want, 0 would be the beginning
print(my_file.read())
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)


# readline() - allows us to read a specific line of code or text starting from the beginning of the file

print(my_file.readline())  # line 1
print(my_file.readline())  # line 2
my_file.seek(0)


# readlines() - gives a list that contains  the entire file
# \n stands for new line
print(my_file.readlines())


# you must manually close the file after you opened it, this will allow you to use it somewhere else in the program
# close() - closes the file
my_file.close()
