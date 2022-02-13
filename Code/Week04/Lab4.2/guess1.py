# This program asks the user to guess a number 
# and stops when they get it right.
# Author: Eret Haava

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)

