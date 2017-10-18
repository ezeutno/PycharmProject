class Account:
    def __init__(self, balance):
        self.__balance = balance

    def getBalance(self):
        return 'Rp. '+ str(self.__balance)

    def deposit(self, amt):
        self.__balance = str(float(self.__balance) + amt)
        print('You have deposit Rp. ' + str(amt))
        return self.__balance

    def withdraw(self, amt):
        if float(self.__balance) >= amt:
            self.__balance = str(float(self.__balance) - amt)
            print('You have withdraw Rp. '+ str(amt))
            return self.__balance
        else:
            print('Sorry your balance is insufficient.')
