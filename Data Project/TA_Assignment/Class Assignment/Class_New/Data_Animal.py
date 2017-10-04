class animal():
    def __init__(self, name, type, data_type, counter, listing, price):
        self.listing = listing
        self.type = type
        self.counter = counter
        self.name = name
        self.data_type = data_type
        self.price = price

    def print_animal(self):
        for i, j in self.type.items():
            if self.data_type == i:
                print(i)
                print('Type ', j[0], '\nGender ', j[1], '\nPrice $', j[2], '\nStock', j[3])

    def counter_cheker(self):
        y = 0
        for i, j in self.type.items():
            if self.data_type == i:
                if j[-1] > 0:
                    y = 1
                else:
                    y = 0
        return y

    def buy(self):
        m = 0
        while m == 0 :
            for a, j in self.type.items():
                if self.data_type == a:
                    print('Are you sure you want to buy', a, '(Y/N)?', end='')
                    y = input()
                    if y.upper() == 'Y':
                        while True:
                            self.counter = int(input('How many do you want to buy?'))
                            if self.counter <= j[-1]:
                                for i in range(self.counter):
                                    self.price.append(j[-2])
                                    j[-1] -= 1
                                    self.listing.append(a)
                                print("Your purchase \n", set(self.listing), '\nYour Total Price $', sum(self.price))
                                break
                            else:
                                print('Sorry our stock only got ', j[-1])
                        m = 1
                    elif y.upper() == 'N':
                        m = 1

    def all_purchase(self):
        if len(self.listing) != 0:
            print('Your purchase \n', set(self.listing), '\nYour Total Price $', sum(self.price))
        print('Thank You for Visiting')
