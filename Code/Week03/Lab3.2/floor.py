# This program floors a number.
# This means, it takes in a float and outputs an int rounded down.
# Your input can also be integer 5, then: 5.0 floored is -5.
# When you're input is negative float, -2.2, then: -2.2 floored is -3.
# You will need the math module math.floor() to do this.
# Author: Eret Haava

import math

numberTofloor = float(input('Enter a float number: '))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}.' .format(numberTofloor, flooredNumber))
