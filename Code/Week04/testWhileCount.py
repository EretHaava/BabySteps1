# Messing with while loops.
# Author: Eret Haava

# while condition:
# statements

count = 0                       # counter controlled loop
while count < 10:
    print(count)
    count = count + 1

count = 10                      # counter controlled loop
while count >= 0:
    print(count)
    count -= 1
print ("Blast Off")

# Sentinel controlled loop
# The program keeps doing something until you enter 
# exactly what's the condition, in this case letter 'q'.
val = input("Enter something (q to quit):")     
while val != 'q':
    print ("You said: " + val)
    val = input("(q to quit):")
print ("Goodbye!")

