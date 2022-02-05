# This program reads in a string and outputs
# every n character of that string.
# You need to use Python's built-in function
# slice[start:stop:step] = slice[::n] to do that.
# n represents in every which character you 
# need to get.
# When doing its job, empty space between 
# the words counts as 1 character.
# Author: Eret Haava

string = input('Enter a string: ')
n = 1
slice = string[::n]
print(slice)

