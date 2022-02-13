# This program generates 10 random numbers,
# prints them out and then prints out the top 3.
# List [] is used to store and manipulate the numbers.
# You can set the range and will it be top 3 or top 7.
# Author: Eret Haava

import random
howMany    = 10
topHowMany = 3
rangeFrom  = 0
rangeTo    = 100

numbers = []

for i in range(0, 10):      # for i in range(rangeFrom, howMany)
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}" .format(howMany,numbers))

# I am keeping the original list maybe I don't need to 
topOnes = numbers.copy()
topOnes.sort(reverse = True)   # if you change this to False, top 3 will be printed out increasing order.
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))
