# This program rounds a number.
# It takes in a float and outputs an int(rounded up or down).
# If accuracy is essential, do not use,
# because it rounds to the nearest even number.
# 4.5 rounds to 4
# but 5.5 rounds to 6
# Author: Eret Haava

numberToRound = float(input('Enter a float number: '))
roundedNumber = round(numberToRound)
print('{} rounded is {}' .format(numberToRound, roundedNumber))
