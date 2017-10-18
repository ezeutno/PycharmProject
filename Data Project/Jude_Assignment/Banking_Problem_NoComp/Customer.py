from Account import Account
import random
class Customer():
    def __init__(self, firstname, lastname, account, balance):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__account = account
        self.__balance = balance

    def getFirstName(self):
        return self.__firstname
    def getLastName(self):
        return self.__lastname
    def getAccount(self):
        return self.__account
    def setAccount(self,acc,amt):
        self.__account = acc
        Account(self.__balance).deposit(amt)
    def newAccount(self,acc,data):
        acc_data = acc+str(random.randint(0,999))
        data.append([acc_data,'0'])
        return acc_data



