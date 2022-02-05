# This program prints out randon fruit by using list[].
# Author: Eret Haava

import random
fruits = ['Apple', 'Banana', 'Orange', 'Pear']
index = random.randint(0, len(fruits)-1)
fruit = fruits[index]

print('A Random Fruit: {}' .format(fruit))

# For this example you should use a tuple(), 
# because you don't change the list.
# Check out randonFruit2.py.
# The functionality of the program will not change.

