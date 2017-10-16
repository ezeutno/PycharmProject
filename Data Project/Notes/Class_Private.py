class Account:
    def __init__(self,balance):
        self.__balance = balance
    def setBalance(self,amt):
        self.__balance = amt
    def getBalance(self):
        return self.__balance
    def deposit(self,amt):
        if amt > 0 :
            self.__balance += amt
    def withdraw(self,amt):
        if amt <= self.__balance:
            self.__balance -= amt


acc = Account(1000)
acc.__balance = 1345
print(acc.getBalance())