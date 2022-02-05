# Why does this message cause an error?

message = 'I have eaten ' + 99 + ' burritos.'
print(message)

# Because you can't concatenate string with integer.
# This program converts an integer into a string.
# Author: Eret Haava

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)
message = 'I have eaten ' + '99' + ' burritos.'
print(message)

