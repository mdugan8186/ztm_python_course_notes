# ==== file io errors ====

# one of the common patterns when working with files is to put them into a try/ except block

try:
    with open('app/sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    # we can even raise this error of we want
    raise err
# another common except is the IOError. an IOError usually happens  whe the computer  or the machine you're on has some issue reading or writing or  doing any sort of IO operation
except IOError as err:
    print('IO error')
    raise err
