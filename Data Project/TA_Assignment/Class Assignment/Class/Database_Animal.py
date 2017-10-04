class animal(object):

    def __init__(self, animal_type, type, choose, total, listing):
        self.type = type
        self.choose = choose
        self.animal_type = animal_type
        self.total = total
        self.listing = listing

    def print_animal_type(self):
        for i,j in self.type.items():
            if self.choose == i :
                print(i)
                if j[2] > 0:
                    print(self.animal_type ,'Type ', j[0], '\n',self.animal_type,'Price $', j[1], '\n',self.animal_type,'Stock ', j[2])
                else:
                    print('Sorry We\'re OUT OF STOCK')

    def choose_animal(self):
        for i,j in self.type.items():
            if self.choose == i :
                self.listing.append(i)
                self.total.append(j[1])
                j[2] -= 1
                print ('You have purchase : {0}. \nYour Total is $ {1}'.format(self.listing,sum(self.total)))

    def stock_checker(self):
        p = False
        for i,j in self.type.items():
            if self.choose == i :
                if j[2] > 0:
                    p = True
        return p

    def all_purchase(self):
        print('You have purchase : {0}. \nYour Total is $ {1}'.format(self.listing,sum(self.total)))