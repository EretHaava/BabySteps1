# This program ask the user to enter a number
# and only stops when the user enters -1.
# Author: Eret Haava

val = input('Enter something (-1 to quit): ')
while val != '-1':
  print('You picked: ' + val)
  val = input('Try again: ')
print('Finally got it!')