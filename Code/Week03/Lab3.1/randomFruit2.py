# This program prints out randon fruit by using Tuple().
# Author: Eret Haava

import random
fruits = ('Apple', 'Banana', 'Orange', 'Pear')
index = random.randint(0, len(fruits)-1)
fruit = fruits[index]

print('A Random Fruit: {}' .format(fruit))

