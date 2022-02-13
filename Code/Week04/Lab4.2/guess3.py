# This program first generates the random number between 0 to 100.
# Then it asks the user to guess that random number.
# The program will tell the user if they were too high or too low.
# And it stops when they get it right.
# Author: Eret Haava


import random
random_number = random.randint(1, 100)
#print(random_number)

guess = int(input('Please guess the number between 0 to 100: '))
while guess != random_number:
    if guess < random_number:
        print('Too low')
    else:
        print('Too high')
    guess = int(input('Please guess again: '))

print('Well done! Yes, the number was ', random_number)

