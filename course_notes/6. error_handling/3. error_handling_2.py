# ==== error handling 2 ====


def sum(num1, num2):
    try:
        return num1 + num2
    # by just doing accept without any exceptions as a programmer we won't know what the error is and we don't know what went wrong
    except:
        print('something is wrong')

# this will throw a TypeError. to fix this we'll put a try block in our function
# print(sum('1', 2))


# we want to add a specific error so we'll know what went wrong and enter what we want to fix it
def sum2(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('Please enter numbers')


# print(sum2('1', 2))


# a common pattern for error handling is to add 'as err' after the type of error, then adding it to a print statement with an f string. you can not concatenate it into your message. this will give more details about what exactly went wrong
def sum3(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        # this will not work (error object)
        # print('Please enter a number' + err)
        print(f'Please enter numbers {err}')


# print(sum3('1', 2))


# we can also wrap errors together
def sum4(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'ooops {err}')


print(sum4('1', 2))
print(sum4(1, 0))
