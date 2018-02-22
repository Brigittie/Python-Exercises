import random

guessCounter = 0
userName = input('Hello! What is your name?\n')
compNumber = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(userName))
while guessCounter < 6:

    userGuess = int(input('Take a guess: '))
    #a = a+1
    guessCounter += 1

    if userGuess < compNumber:
        print('Your guess is too low.')

    if userGuess > compNumber:
        print('Your guess is too high.')

    if userGuess == compNumber:
        break

if userGuess == compNumber:
    print('Good job, {0}! You guessed my number in {1} guesses!'.format(userName, guessCounter))
else:
    print('Nope. The number I was thinking of was {0}'.format(compNumber))
