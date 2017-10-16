class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = int(balance)
        self.balance = 0

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def credit(self,amt):
        self.balance += amt
        return self.balance

    def debit(self,amt):
        if amt <= self.balance:
            self.balance -= amt
        else :
            print('Amount exceeded balance')
        return self.balance

    def transferTo(self, anth_acc, amt):
        if amt <= self.balance:
            self.balance -= amt
            anth_acc.balance += amt
        else :
            print('Amount exceeded balance')
        return self.balance

    def toString(self):
        return "Account[id= {0}, name= {1}, balance{2}".format(self.id,self.name,self.balance)