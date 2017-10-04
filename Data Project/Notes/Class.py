class car(object):
    def __init__(self, type, price):
        self.type = type
        self.price = price
    def car_print(self):
        print("This car type is {0} and the price is {1}".format(self.type, self.price))