# This program prints out random number between 1 and 10.
# Author: Eret Haava

import random
number = random.randint(1,10)
print('Here is a random number: {}' .format (number))

# This program tries to guess your number.
# Author: Eret Haava

import random
number1 = random.randint(1,100)
number = input('Between 1 and 100, what number are you thinking about? \nPress Enter')
print('Were you thinking about: {}?' .format (number1))

