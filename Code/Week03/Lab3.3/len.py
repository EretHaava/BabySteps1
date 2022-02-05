# This program reads in a string and outputs it's lenght.
# You use built-in function len() to do that.
# Author: Eret Haava

# If you enter two words, the program counts a space between words 
# as one charachter, two spaces = 2 charachters.
inputString = input('Enter a string: ')
lenghtOfString = len(inputString)
print('The lenght of {} is {} characters.' .format(inputString, lenghtOfString))

