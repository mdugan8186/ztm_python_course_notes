# ==== exercise: guessing game ====

# generate a number 1-10
# get an input from the user
# check that the input is a number that is 1-10
# check if the number is the right guess, otherwise
# ask again

from random import randint

# to have it work from the terminal
import sys
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))


answer = randint(1, 10)
# print(answer)


while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess > 0 and guess < 11:
            if guess == answer:
                print('You got it right')
                break
        else:
            print('I said pick a number between 1 and 10')
    except ValueError:
        print('Please enter a number')
        continue
