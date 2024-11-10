# ==== exercises: error handling ====

while True:
    try:
        age = int(input('What is your age? '))
        10 / age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thank you')
        break
    finally:
        print('OK, I am finally done')
    # because of the break in else this print statement will never print
    print('Can you hear me')

# finally runs at the end after everything has been executed. finally runs regardless of what happens, meaning if the loops is continuing to loop or if the loop breaks
