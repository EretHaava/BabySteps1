# How to convert integer into a string.
# Author: Eret Haava

# By adding quotes '...', Python thinks that 3 is a string and not an integer.
aGe = '3'
print('You are ' + aGe)

# By using str(), we convert integer into a string.
agE = 4
print('You are ' + str(agE))

# Checking variable data type (aGe=str and agE=int)
print(type(aGe))
print(type(agE))

