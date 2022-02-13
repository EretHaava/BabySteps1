# This program reads in numbers until 
# the user enters 0.
# It will print the numbers back out again 
# and after entering 0, it calculates 
# entered numbers average. 
# Author: Eret Haava

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("Enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print ("The average is {}." .format(average))

