# This program reads in a string and outputs
# every n character of that string.
# You need to use Python's built-in function
# slice[start:stop:step] = slice[::n] to do that.
# n represents in every which character you 
# need to get.
# n can be positive or negative.
# If n is positive, the program starts from 
# the beginning of the string and
# outputs every n charachter.
# If n is negative, the program starts from 
# the end of the string and outputs every n character.
# When doing its job, 1 empty space between 
# the words counts as 1 character.
# Author: Eret Haava

string = input('Enter a string: ')
n = -2
slice = string[::n]
print(slice)

