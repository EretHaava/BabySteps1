# This program checks is the number even or odd.
# Author: Eret Haava

myNum = 21
if myNum % 2 == 0:
    print("The number is even number.")
else:
    print("The number is odd number.")

# or you can check is number even or odd in it that way
# use brackets so it's easier to understand in which order the program is doing things

a = 32
isEven = ((a % 2) == 0)     # isEven = a % 2 == 0 - also correct
print('is ', a, 'even?', isEven)

