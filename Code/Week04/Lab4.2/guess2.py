# This program asks the user to guess a number between 0 to 100.
# The program will tell the user if they were too high or too low
# and stops when they get it right.
# Author: Eret Haava

numberToGuess = 30

guess = int(input("Please guess the number between 0 to 100: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)

