from Database_Animal import animal

all_animal = []
p = []
y = []
cat_type = {
    "British Shorthair": ['Domestic Cat', 100, 3],
    "Siamese Cat": ['Breed Cat', 200, 5],
    "Persian Cat": ['Perisan Cat', 400, 3]
}

dog_type = {
    "Spaniel": ['Gun Dog', 100, 0],
    "Terrier": ['Breed', 200, 5],
    "Retriver": ['Hunter', 400, 3]
}

rabbit_type = {
    "Angora": ['Wild Rabbit', 100, 3],
    "Dutch": ['Breed ', 200, 5],
    "Dwarf Hotot": ['Hoppper', 400, 3]
}
print('Welcome to CDR Pet Shop.')
print('We sell Cat, Dog and Rabbit')


def print_animal(a):
    for i in a.keys():
        print(i)


def continue_val(b, c, d, e, f):
    while True:
        j = input('Do you wish to continue?')
        if j.upper() == 'N':
            y.append(12345)
            animal_2 = animal(b, c, d, e, f)
            animal_2.all_purchase()
            break
        elif j.upper() == 'Y':
            break
        else:
            print('Error, Please Try Again!')


def run(b, c, d, e, f):
    animal_2 = animal(b, c, d, e, f)
    animal_2.choose_animal()
    continue_val(b, c, d, e, f)

def sytanx(b,c,d,e,f):
    animal_2 = animal(b, c, d, e, f)
    animal_2.print_animal_type()
    m = animal_2.stock_checker()
    if m == True:
        while True:
            M = input('Are you sure to continue?')
            if M.lower() == 'y':
                run(b,c,d,e,f)
                break
            elif M.lower() == 'n':
                break
            else:
                print('Error, Please try again!(1)')

while y == []:
    x = input('What do you wish to buy?')
    if x.upper() == 'CAT':
        print_animal(cat_type)
        L = input('What type do you wish to buy?').title()
        sytanx(x.upper(), cat_type, L, p, all_animal)
    elif x.upper() == 'DOG':
        print_animal(dog_type)
        L = input('What type do you wish to buy?').title()
        sytanx(x.upper(), dog_type, L, p, all_animal)
    elif x.upper() == 'RABBIT':
        print_animal(rabbit_type)
        L = input('What type do you wish to buy?').title()
        sytanx(x.upper(), rabbit_type, L, p, all_animal)
    elif x.upper() == 'I DON\'T WANT TO BUY' or x.upper() == 'NO, THANK YOU!' or x.upper() =='NO' or x.upper() =='N':
        print('Thank you for visiting CDR Pet Shop.')
        break
    else:
        print('Error, Please Try Again!(2)')