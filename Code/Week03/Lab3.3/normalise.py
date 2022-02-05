# This program reads in a string and strips any leading or trailing spaces.
# It also converts all the letters to lower case.
# It also outputs the lenght of the original string and the normalised one.
# Author: Eret Haava 

rawString = input('Please enter a string: ')
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print('That String nomalised is: {}' .format(normalisedString))
print('We reduced the input string from {} to {} characters.' .format(
    lenghtOfRawString, lenghtOfNormalised))

# strip() gets rid of leading spaces but not spaces between string.
    # Please enter a string:          PlEaSe        CoMe HOME!        
    # That String nomalised is: please        come home!
    # Please enter a string:             PleaSE ComE HOME!
    #That String nomalised is: please come home!

