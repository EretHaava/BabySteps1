# Messing with dictionaries.
# Author: Eret Haava

car = {                                     # car have a 4 key value pairs
    'make' : 'Ford',
    'model' : 'Mondeo',
    'year' : 2006,
    'owner' : {
        'name' : 'Andrew', 
        'driver-number' : 1123
    }
}
print(car['year'])
print(car['owner'])
print(car['owner']['name'])
print(type(car['owner'].get('names')))

# if you want to get the keys out, you do
for x in car:
    print(car[x])

#if you want to get the key and the value
for x, y in car.items():
    print(x, y)


