# This program reads in a students percentage 
# and prints out the corresponding grade.
# However, if the student gets 69.5%, it rounds up
# to Distinction, not down to Merit2, like it should. 
# math.ceil method rounds a number up to nearest integer.
# Author: Eret Haava

percentage = float(input('Enter the percentage: '))
import math
percentage = math.ceil(percentage)

# be careful with ands and ors
if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")
