# Testing if + elif + else
# Author: Eret Haava

aNumber = 11
if (aNumber % 2) == 0:          # I did not need brackets, in for clarity
    print(aNumber, 'is even')   # another way of printing variables
elif (aNumber % 3) == 0:        # if the number is even this will not be checked
    print(aNumber, 'is divisable by 3')
else:
    print(aNumber, 'is not even or divisable by 3')

print('this will always be outputted')

