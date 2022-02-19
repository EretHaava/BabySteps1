# More messing with dictionaries.
# Here we're checking out loops.
# Author: Eret Haava

car = {                                    
    'make' : 'Fiat',
    'model' : 'Punto',
    'price' : 10000,
    'tags' : ['pre-owned', 'BestBuy', 'Dealer']
}

print(car)

for key, value in car.items():
    print(key, ' has value ', car[key])

for key, value in car.items():
    print(key, ' has value ', value)



