# This program will tells youthe lenght of your name
# and how old you will be within a year.
# Author: Eret Haava

print('Hello! \nWhat is your name?')
myName = input()
print('It is good to meet you, ' + myName + '!')
print('The lenght of your name is: ' )
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

