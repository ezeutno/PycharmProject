from Customer import Customer
import random

class Bank(Customer):
    def __init__(self,customers,numberOfCustomers, bankName):
        self.__customers = customers
        self.__numberOfCustomer = int(numberOfCustomers)
        self.__bankName = bankName
        Customer.__init__(self,'0','0','0','0')

    def addCustomer(self, f, l):
        while True:
            username = '17650'+str(random.randint(1000,9999))
            count = 0
            for i in self.__customers:
                if username == i[0]:
                    continue
                else :
                    count += 1
            if count == len(self.__customers):
                break
        self.__customers.append([username,[f,l],[]])
        return 'Your username is {0}.'.format(username)

    def getNumOfCustomers(self):
        return self.__numberOfCustomer

    def getCustomers(self,index):
        return self.__customers[index][0]

