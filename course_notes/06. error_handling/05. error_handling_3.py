# ==== error handling 3 ====

while True:
    try:
        age = int(input('What is your age? '))
        10 / age
        # raise ValueError('Hey cut it out')
        raise Exception('Hey cut it out')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('OK, I am finally done')


# raise
# it is rare that you have to do this but its possible to throw your own error with raise. you can enter whatever error you want to insert followed by a message.
# instead of an error you can also throw an Exception
