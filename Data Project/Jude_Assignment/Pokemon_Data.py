import random

pokemon_data = {
    "Ivysaur": ['Grass', 'Poison', 'Male', 60, 62, [random.randint(-3, 3), random.randint(-3, 3)]],
    "Charizard": ['Fire', 'Flying', 'Male', 78, 84, [random.randint(-3, 3), random.randint(-3, 3)]],
    "Butterfree": ['Bug', 'Flying', 'Female', 60, 45, [random.randint(-3, 3), random.randint(-3, 3)]]
}

location = [0, 0]
count = 0
capture = []


class Instuction:
    def __init__(self, location, data, capture):
        self.location = location
        self.data = data
        self.capture = capture

    def move_location(self, input_location, amt):
        if input_location.upper() == 'R':
            self.location[0] += amt
        elif input_location.upper() == 'L':
            self.location[0] -= amt
        elif input_location.upper() == 'U':
            self.location[1] += amt
        elif input_location.upper() == 'D':
            self.location[1] -= amt
        else:
            print('Error!')

    def detection_pokemon(self):
        for i, j in self.data.items():
            print(i, j[-1])
            if self.location == j[-1]:
                print(
                    'Your found! \nName : {0} \nType : {1} \nFeature : {2} \nGender : {3} \nAttack : {4} \nHP : {5}'.format(
                        i, j[0], j[1], j[2], j[3], j[4]))
                y = input('Do you want to capture it?')
                if y.upper() in ['Y', 'YES', 'YUP']:
                    self.capture.append(i)
                    j[-1] = [random.randint(-3, 3), random.randint(-3, 3)]
                elif y.upper() in ['N', 'NO', 'NOPE']:
                    j[-1] = [random.randint(-3, 3), random.randint(-3, 3)]
                else:
                    print('Error!')


z = 0

while z == 0:
    x = input('Where do you want to move? (R,L,U,D) ')
    move = int(input('How many do you want to move? '))
    m = Instuction(location, pokemon_data, capture)
    m.move_location(x, move)
    print('Your Location is ', location)
    m.detection_pokemon()
    while True:
        l = input('Do you wish to continue? ')
        if l.upper() in ['Y', 'YES', 'YUP']:
            z = 0
            break
        elif l.upper() in ['N', 'NO', 'NOPE']:
            z = 1
            break
    print('You have capture', capture)
