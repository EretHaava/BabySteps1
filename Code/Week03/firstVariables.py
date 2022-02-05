# Python is case-sensitive.
# Type() function will tell us variable data type.
# Variable have to be only one word, 
# you can use letters, numbers and the underscore (_) charachter 
# but it can't begin with a number.
# Author: Eret Haava

Age = 32
# boolean
aGe = True
# string (quotes and double quotes, no difference)
agE = 'Hello!'
AGE = "Hello You!"
print(type(Age))
print(type(aGe))
print(type(agE))
print(type(AGE))

# More practise, pay attention to agE and AGE, both are strings!
age = 3
aGe = {4}
agE = '5'
AGE = 'Hello'
print('Type of age is: ' + str(type(age)))
print('Type of aGe is: ' + str(type(aGe)))
print('Type of agE is: ' + str(type(agE)))
print('Type of SGE is: ' + str(type(AGE)))

# Making things more complicated. 
# Messing around with variable types. 
# By surrounding 41 with quotes, we converted it into a string!
age_1 = '41'
print('You are ' + str(age_1) + ' years old.')
nextYear = int(age_1) + 1
print('Next year You will be '+ str(nextYear) + '!')

# Converting str to int and int to str.
# Next two programs both work, however
# in first one age=int and second one age=str.
# Because I converted age into string (2nd one),
# I don't have to convert age into a string on first print.
# However, 2nd print in both cases you have to convert/use str()  
# becuase you can't add 1 onto a string.

age_1 = 41
print('You are ' + str(age_1) + ' years old.')
nextYear = int(age_1) + 1
print('Next year You will be '+ str(nextYear) + '!')

age_1 = '41'
print('You are ' + age_1 + ' years old.')
nextYear = int(age_1) + 1
print('Next year You will be '+ str(nextYear) + '!')