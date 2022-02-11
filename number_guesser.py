import random

turns = 0
bound = input('Please type a number bigger than 10 (This will set the boundary of random numbers): ')

if bound.isdigit():
    bound = int(bound)

    if bound < 10:
        print('Please type a number of at least 10.')
        quit()
else: 
    print('Please type a number next time.')
    quit()

number = random.randint(0, bound)

while True:
    guess = input('Your guess: ')
    turns += 1
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number next time.')
        continue

    if guess == number:
        print(f'You got it in {turns} turns.')
        break
    elif guess > number:
        print(f'You got it wrong! The number is smaller than {guess}.')
    else:
        print(f'You got it wrong! The number is bigger than {guess}.')