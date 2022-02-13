# This program asks to input a number
# and then tells is the number even or odd.
# Author: Eret Haava

number = int(input('Enter a number: '))
if (number % 2) == 0:
    print('{} is an even number.' .format(number))
else:
    print('{} is an odd number.' .format(number))

