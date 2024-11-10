# ==== file paths ====

# to get to files in other directories use the name of the folder followed by a forward slash then the name of the file you are trying to access

# this is called a relative path. it's relative to the directory that you are running the script from
# most of the time you will see relative because it is a lot simpler
with open('app/sad.txt', mode='r') as my_file:
    print(my_file.read())

# this is called an absolute path because it is is giving an absolute path
with open('/home/mdugan8186/udemy/andrei-neagoie/python/course_notes/10. file_io/3. file_paths/app/sad.txt', mode='r') as my_file:
    print(my_file.read())


# you may also see a ./ which means from the current folder
with open('./app/sad.txt', mode='r') as my_file:
    print(my_file.read())


# pathlib can help you take care of filesystems when writing programs that will be on different types of operating systems (linux, mac, windows)
# https://docs.python.org/3/library/pathlib.html
