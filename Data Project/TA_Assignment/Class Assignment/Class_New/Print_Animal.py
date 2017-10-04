from Data_Animal import *

all_animal = []
price= []
count = 0
y = []

cat_type = {
    "Shimmer" : ["Breed", 'Male', 300, 0],
    "Janner" : ["Domenstic", 'Female', 400, 40],
    "Yammen" : ["Tuskan",'Male', 500, 32 ]
}

dog_type = {
    "Huskey" : ["Local",'Male', 400, 4],
    "Hunter" : ["Running",'Female', 200, 5],
    "Donkey" : ["Slow",'Female', 200, 40],
    "Raindear" : ["Local", 'Male', 300, 0]
}

rabbit_type = {
    "Greyhound" : ['Chincila', 'Male', 500, 4],
    "Hungky" : ['Albino', 'Female', 600, 5],
    "Bunter" : ['Chinbilno', 'Male', 400,3]
}

def print_local(a):
    for i in a.keys():
        print(i)

def choose(name, type, counter,listing,price):
    print('What type of', name.lower(), 'do you wish to buy?', end = ' ')
    x = input()
    animal2 = animal(name, type, x.title(), int(counter), listing, price)
    animal2.print_animal()
    if animal2.counter_cheker() == 1:
        animal2.buy()
    else :
        print('Since we are out off stock!')
    while True :
        m = input('Do you wish to continue? (Y/N) ')
        if m.upper() == 'Y':
            break
        elif m.upper() == 'N':
            animal2.all_purchase()
            y.append(12345)
            break

print('Welcome to Counter Pet Shop.\nWe sell Cat, Dog and Rabbit')
while y ==[] :
    try :
        x = input('What do you wish to buy? (Cat, Dog or Rabbit)?')
        if x.upper() == 'CAT':
            print_local(cat_type)
            choose(x.upper(), cat_type, count, all_animal, price)
        elif x.upper() == 'DOG':
            print_local(dog_type)
            choose(x.upper(), dog_type, count, all_animal, price)
        elif x.upper() == 'RABBIT':
            print_local(rabbit_type)
            choose(x.upper(), rabbit_type, count, all_animal, price)
        else:
            print('Error, Please try again!')
    except:
        print('Error, Please try again!')
