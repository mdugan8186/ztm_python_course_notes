# ==== exercise: testing ====

from random import randint


def run_guess(guess, answer):
    if not isinstance(guess, int):
        raise ValueError('Guess must be a number')

    if guess > 0 and guess < 11:
        if guess == answer:
            print('You got it right')
            return True
    else:
        print('I said guess a number between 1-10')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    print(answer)

    while True:
        try:
            guess = int(input('Guess a number between 1-10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('Please enter a number')
            continue
