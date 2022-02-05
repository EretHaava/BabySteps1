# This program takes in money in dollars
# and outputs money in cents.
# When dealing with money, always use integer values not floating-point values.
# Author: Eret Haava


amount = float(input('Please enter an amount: '))
# amount = float(input('Please enter an amount in dollars: ')) # to be more specific
# To get rid of negative cents, use absolute value: abs()
cents = abs(int(amount * 100)) 
print('That amount in cents is: {}.' .format(cents))

# This program takes in money in cents
# and outputs money in dollars.
# Author: Eret Haava

amount = int(input('Please enter an amount: '))
# amount = int(input('Please enter an amount in cents: ')) # to be more specific
# To get rid of negative dollars, use absolute value: abs()
dollars = abs(float(amount / 100)) 
print('That amount in dollars is: {}.' .format(dollars))
