# This program checks variable types and then outputs them.
# Author: Eret Haava 

i = 3
fl = 3.5
isa = True
memo = 'How Now Brown Cow'
lots = []

print(type(i))
print(type(fl))
print(type(isa))
print(type(memo))
print(type(lots))

print('Variable {} is of type: {} and value: {}.' .format('i', type(i), i))
print('Variable {} is of type: {} and value: {}.' .format('fl', type(fl), fl))
print('Variable {} is of type: {} and value: {}.' .format('isa', type(isa), isa))
print('Variable {} is of type: {} and value: {}.' .format('memo', type(memo), memo))
print('Variable {} is of type: {} and value: {}.' .format('lots', type(lots), lots))


# I found the first option a bit confusing, therefore I changed the variable names,
# then checked their data types and put them into a sentence. 
# A bit longer process but makes sense (not so confusing) for me...
# Author: Eret Haava

a = 3                           # integer
b = 3.5                         # float
c = True                        # boolean
d = 'How Now Brown Cow'         # string
e = [1, 2, 3, 4, 5]             # list

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print('Variable {} is of type: {} and value: {}.' .format('a', type(a), a))
print('Variable {} is of type: {} and value: {}.' .format('b', type(b), b))
print('Variable {} is of type: {} and value: {}.' .format('c', type(c), c))
print('Variable {} is of type: {} and value: {}.' .format('d', type(d), d))
print('Variable {} is of type: {} and value: {}.' .format('e', type(e), e))



