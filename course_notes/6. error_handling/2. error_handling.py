# ==== error handling ====

# asking a users age and making sure it is a number with int(). if a non number is entered a ValueError will be thrown

# to handle errors in a given block of code use try and except. place your block of code in try. place what you want to code to do if it throws n error in the except

# to keep running the code if an error is thrown we can use a while loop

# to stop the while loop from repeating if there are no errors we use an else statement with the keyword break


while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except:
        print('Please enter a number')
    else:
        print('Thank you')
        break


# the try except else block can go anywhere, we could wrap our entire file if we wanted to. we can add it to our functions (each individual function)


# in the except block we can give it what type of error we want to handle, but it will only except those types of errors, any other type of error will throw an error and stop the program. to fix this we can have multiple excepts to catch different errors

while True:
    try:
        age2 = int(input('How old are you? '))
        # giving 0 will give a ZeroDivisionError
        10 / age2
    except ValueError:
        print('Please enter a valid age')
    except ZeroDivisionError:
        print('Please enter age higher than zero')
    else:
        print('Thanks')
        break


# the except block will only run once and then come back to the while loop
