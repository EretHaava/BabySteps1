# This program takes in a number and outputs its absolute value.
# The number can be negative or positive, an integer number
# or floating-point number.
# You will always get an answer and the answer will always be 
# a floating-point number.
# Author: Eret Haava

number = float(input('Enter a number: '))
absoluteValue = abs(number)
print('The absolute value of {} is {}.' .format(number, absoluteValue))

# If you want, you can specify your question:
#                                 'Enter an integer number: ' 
#                                 'Enter a floatint-point number: '
# The idea of the both programs is the same, however
# first one takes in and outputs a floating-point number
# second one takes in and outputs an integer number.

# You can use both floating-point and integer numbers
# with this program.
# However, even when entering an integer number, 
# the output is always floating-point number.
number = float(input('Enter a floating-point number: '))
absoluteValue = abs(number)
print('The absolute value of {} is {}.' .format(number, absoluteValue))

# You can only use integer numbers with this program!
# Output will be an integer number.
# However, when entering floating-point number into this program, 
# it will give you an error,  
# therefore it will be safer to use float option.
number = int(input('Enter an integer: '))
absoluteValue = abs(number)
print('The absolute value of {} is {}.' .format(number, absoluteValue))
